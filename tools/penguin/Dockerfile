# Dockerfile for Penguin
# Pseudouridine detection tool using XGBoost

FROM python:3.9-slim

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="Penguin - A tool for predicting pseudouridine sites in direct RNA nanopore sequencing"

ARG VERSION=1.0.0

# Install build tools + compile pysam and xgboost (with C extensions) + purge build tools
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
        git+https://github.com/Janga-Lab/Penguin.git@${VERSION} && \
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
        xgboost \
        pandas \
        numpy

# Set working directory
WORKDIR /data

# Verify installation
RUN python -c "import xgboost; print('XGBoost:', xgboost.__version__)" && \
    penguin --help

# Default command
CMD ["penguin", "--help"]
