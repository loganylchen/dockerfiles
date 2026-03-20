# Dockerfile for NanoPsu (Nanopore_psU)
# Pseudouridine detection tool using TensorFlow

FROM python:3.9-slim

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="NanoPsu - Pseudouridine site prediction from nanopore RNA direct sequencing"

ARG VERSION=1.0.0

# Install build tools + compile pysam (with C extension) + purge build tools
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
        git+https://github.com/sihaohuanguc/Nanopore_psU.git@${VERSION} && \
    apt-get purge -y --auto-remove \
        gcc \
        git \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install TensorFlow (CPU-only) and additional dependencies
RUN pip install --no-cache-dir \
        tensorflow-cpu==2.13.0 \
        pandas \
        numpy

# Set working directory
WORKDIR /data

# Verify installation
RUN python -c "import tensorflow; print('TensorFlow:', tensorflow.__version__)" && \
    nanopsu --help

# Default command
CMD ["nanopsu", "--help"]
