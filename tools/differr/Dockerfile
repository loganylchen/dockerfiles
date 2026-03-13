FROM debian:bookworm-slim

ARG VERSION=0.2

# Install build tools + compile differr (with pysam C extension) + purge build tools,
# all in one layer so build artifacts never persist in the image.
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
    pip3 install --no-cache-dir --break-system-packages \
        git+https://github.com/bartongroup/differr_nanopore_DRS.git@${VERSION} && \
    apt-get purge -y --auto-remove \
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
