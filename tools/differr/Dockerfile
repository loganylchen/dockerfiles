FROM python:3.5-slim

ARG VERSION=0.2

# Install build tools + compile differr (with pysam C extension) + purge build tools,
# all in one layer so build artifacts never persist in the image.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        git \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        ca-certificates && \
    pip install --no-cache-dir \
        git+https://github.com/bartongroup/differr_nanopore_DRS.git@${VERSION} && \
    apt-get purge -y --auto-remove \
        gcc \
        git \
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
