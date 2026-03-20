# Build stage
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION=dd0ccc81
ARG SAMTOOLSVER=1.19.2

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libncurses-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        git && \
    rm -rf /var/lib/apt/lists/*

# Build samtools from source
WORKDIR /tmp
RUN curl -L https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 | tar -jxf - && \
    cd samtools-${SAMTOOLSVER} && \
    ./configure --without-curses && \
    make && \
    strip samtools

# Clone DRUMMER at the specified commit
RUN git clone https://github.com/loganylchen/DRUMMER.git /opt/DRUMMER && \
    cd /opt/DRUMMER && \
    git checkout ${VERSION} && \
    # Fix Python 3 compatibility: 'rU' mode is removed in Python 3
    sed -i "s/open(transcriptome_file,'rU')/open(transcriptome_file,'r')/g" modules/test_exome.py && \
    sed -i "s/open(transcriptome_file, \"rU\")/open(transcriptome_file, \"r\")/g" modules/test_exome.py

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG SAMTOOLSVER=1.19.2

# Install runtime dependencies + pip packages in one layer (no build tools needed
# for pure-Python deps, so no purge step required)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        bedtools \
        zlib1g \
        libbz2-1.0 \
        liblzma5 \
        libcurl3-gnutls \
        libssl3 \
        ca-certificates && \
    pip3 install --no-cache-dir --break-system-packages \
        seaborn \
        scipy \
        pandas \
        numpy \
        biopython \
        matplotlib \
        statsmodels && \
    ln -sf /usr/bin/python3 /usr/local/bin/python && \
    rm -rf /var/lib/apt/lists/*

# Copy samtools binary and DRUMMER from builder
COPY --from=builder /tmp/samtools-${SAMTOOLSVER}/samtools /usr/local/bin/samtools
COPY --from=builder /opt/DRUMMER /opt/DRUMMER

# Install wrapper script
COPY DRUMMER /usr/local/bin/DRUMMER
RUN chmod +x /usr/local/bin/DRUMMER

# Smoke-test
RUN samtools --version | head -1 && \
    DRUMMER -h

WORKDIR /data

CMD ["DRUMMER", "-h"]
