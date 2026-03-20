# Dockerfile for NanoMUD
# Deep learning framework for detecting pseudouridine and N1-methylpseudouridine

FROM python:3.9-slim

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="NanoMUD - Deep learning framework for detecting uridine modifications (pseudouridine and m1Psi) using Nanopore DRS"

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
        torch==2.0.1 \
        torchvision==0.15.2 \
        --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir \
        git+https://github.com/ABOMSBI/NanoMUD.git@${VERSION} && \
    apt-get purge -y --auto-remove \
        gcc \
        git \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install additional dependencies
RUN pip install --no-cache-dir \
        pandas \
        numpy

# Set working directory
WORKDIR /data

# Verify installation
RUN python -c "import torch; print('PyTorch:', torch.__version__)" && \
    nanomud --help

# Default command
CMD ["nanomud", "--help"]
