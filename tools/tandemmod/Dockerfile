# Multi-stage build for TandemMod
# Stage 1: Builder - Install build dependencies and PyTorch
FROM python:3.9-slim AS builder

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="TandemMod - Deep learning framework for detecting RNA modifications in nanopore DRS data"

ARG VERSION=1.0.0

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        gcc \
        g++ \
        && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install PyTorch with CPU-only version (smaller image)
# Using specific versions for compatibility
RUN pip install --no-cache-dir \
        torch==2.0.1 \
        torchvision==0.15.2 \
        --index-url https://download.pytorch.org/whl/cpu

# Install TandemMod from GitHub
RUN pip install --no-cache-dir \
        git+https://github.com/yulab2021/TandemMod.git@${VERSION}

# Install remaining dependencies
RUN pip install --no-cache-dir \
        pandas \
        numpy \
        scikit-learn \
        pyyaml

# Stage 2: Runtime - Minimal image
FROM python:3.9-slim

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="TandemMod - Deep learning framework for detecting RNA modifications in nanopore DRS data"

ARG VERSION=1.0.0

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgomp1 \
        && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Set working directory
WORKDIR /data

# Verify installation
RUN python -c "import torch; print('PyTorch:', torch.__version__)" && \
    tandemmod --help

# Default command
CMD ["tandemmod", "--help"]
