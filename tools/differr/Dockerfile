FROM debian:bookworm-slim

ARG VERSION=0.2

# Install runtime deps + build tools needed to compile pysam C extensions
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install differr and all dependencies
RUN pip3 install --no-cache-dir --break-system-packages \
        git+https://github.com/bartongroup/differr_nanopore_DRS.git@${VERSION}

# Remove build tools after pip compilation
RUN apt-get purge -y --auto-remove \
        gcc \
        python3-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Smoke-test
RUN differr --help

WORKDIR /data

CMD ["differr", "--help"]
