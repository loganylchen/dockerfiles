# Multi-stage build for RNANO
# Stage 1: Builder - Install build dependencies and PyTorch
FROM python:3.9-slim AS builder

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="RNANO - NLP-based deep learning tool for RNA modification detection from Nanopore DRS"

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

# Install PyTorch with CPU-only version
RUN pip install --no-cache-dir \
        torch==2.0.1 \
        --index-url https://download.pytorch.org/whl/cpu

# Install RNANO from GitHub
RUN pip install --no-cache-dir \
        git+https://github.com/abhhba999/RNANO.git@${VERSION}

# Install remaining dependencies
RUN pip install --no-cache-dir \
        transformers \
        pandas \
        numpy \
        scikit-learn \
        tqdm \
        huggingface_hub \
        pyyaml

# Stage 2: Runtime - Minimal image
FROM python:3.9-slim

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="RNANO - NLP-based deep learning tool for RNA modification detection from Nanopore DRS"

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
RUN python -c "import torch; import transformers; print('Dependencies OK')" && \
    rnano --help

# Default command
CMD ["rnano", "--help"]
