# Dockerfile for PsiNanopore (psipore)
# Pseudouridine detection tool for nanopore direct RNA sequencing

FROM python:3.9-slim

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="PsiNanopore - Pseudouridine detection from nanopore direct RNA sequencing"

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
        git+https://github.com/RouhanifardLab/PsiNanopore.git@${VERSION} && \
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
        numpy \
        pandas \
        scikit-learn

# Create psipore wrapper script
RUN echo '#!/bin/sh' > /usr/local/bin/psipore && \
    echo 'python -m psipore "$@"' >> /usr/local/bin/psipore && \
    chmod +x /usr/local/bin/psipore

# Set working directory
WORKDIR /data

# Verify installation
RUN python -c "import psipore; print('psipore installed')"

# Default command
CMD ["psipore", "--help"]
