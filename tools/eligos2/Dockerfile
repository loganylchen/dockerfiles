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

# Install runtime dependencies:
# - python3 + pip for eligos2 Python packages
# - r-base for R/rpy2 integration
# - bedtools for pybedtools
# - runtime shared libs needed by samtools and Python C extensions
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        r-base \
        bedtools \
        gawk \
        zlib1g \
        libbz2-1.0 \
        liblzma5 \
        libcurl4 \
        libssl3 \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages (no cache)
RUN pip3 install --no-cache-dir --break-system-packages \
        pysam \
        pandas \
        pybedtools \
        rpy2 \
        tqdm \
        numpy

# Install R package samplesizeCMH (needed for CMH test in eligos2)
RUN Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")' && \
    rm -rf /tmp/downloaded_packages /root/.R

# Remove gcc after Python packages are compiled (it was only needed for C extensions)
RUN apt-get purge -y --auto-remove gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

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
