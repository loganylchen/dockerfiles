# Build stage
FROM debian:bookworm-slim AS builder

ARG VERSION=2.1.0
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

# Clone eligos2 at the specified version tag
RUN git clone --depth=1 --branch v${VERSION} https://gitlab.com/piroonj/eligos2.git /opt/eligos2 && \
    chmod +x /opt/eligos2/*.py /opt/eligos2/Scripts/* 2>/dev/null || true

# Runtime stage
FROM debian:bookworm-slim

ARG VERSION=2.1.0
ARG SAMTOOLSVER=1.19.2

# Install build tools + runtime deps, compile Python packages (rpy2/pysam need
# make + r-base-dev + gcc), install R package, then purge build tools —
# all in one layer so build artifacts never persist in the image.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        make \
        r-base \
        r-base-dev \
        bedtools \
        gawk \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        ca-certificates && \
    pip3 install --no-cache-dir --break-system-packages \
        pysam \
        pandas \
        pybedtools \
        rpy2 \
        tqdm \
        numpy && \
    Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")' && \
    apt-get purge -y --auto-remove \
        python3-dev \
        gcc \
        make \
        r-base-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/downloaded_packages /root/.R

# Copy samtools binary from builder
COPY --from=builder /tmp/samtools-${SAMTOOLSVER}/samtools /usr/local/bin/samtools

# Copy eligos2 from builder
COPY --from=builder /opt/eligos2 /opt/eligos2

# Add eligos2 to PATH and create python symlink
RUN ln -sf /usr/bin/python3 /usr/local/bin/python

ENV PATH="/opt/eligos2:/opt/eligos2/Scripts:${PATH}"

# Smoke-test
RUN samtools --version | head -1 && \
    eligos2 -h

WORKDIR /data

CMD ["eligos2", "-h"]
