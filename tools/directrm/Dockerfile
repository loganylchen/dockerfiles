# Multi-stage build for DirectRM
# Stage 1: Builder - Install build dependencies and PyTorch
FROM python:3.9-slim AS builder

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="DirectRM - Integrated detection of 6 abundant RNA modifications from nanopore DRS"

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
# Using CUDA-compatible version for CPU fallback
RUN pip install --no-cache-dir \
        torch==2.1.2 \
        torchvision==0.16.2 \
        --index-url https://download.pytorch.org/whl/cpu

# Clone DirectRM repository (includes pre-trained models)
WORKDIR /opt
RUN git clone https://github.com/yuxinPenny/DirectRM.git && \
    cd DirectRM && \
    git checkout ${VERSION} || echo "Using default branch"

# Install DirectRM dependencies
RUN pip install --no-cache-dir \
        einops \
        transformers \
        faiss-cpu \
        statsmodels \
        upsetplot \
        xgboost

# Install additional Python dependencies
RUN pip install --no-cache-dir \
        pandas \
        numpy \
        scikit-learn \
        scipy \
        tqdm \
        pyyaml \
        matplotlib

# Stage 2: Runtime - Minimal image
FROM python:3.9-slim

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="DirectRM - Integrated detection of 6 abundant RNA modifications from nanopore DRS"

ARG VERSION=1.0.0

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgomp1 \
        && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy DirectRM from builder
COPY --from=builder /opt/DirectRM /opt/DirectRM

# Add DirectRM scripts to PATH
ENV PATH="/opt/DirectRM/scripts:$PATH"
ENV PYTHONPATH="/opt/DirectRM:$PYTHONPATH"

# Set working directory
WORKDIR /data

# Verify installation
RUN python -c "import torch; print('PyTorch:', torch.__version__)" && \
    python -c "import transformers, faiss; print('Dependencies OK')" && \
    ls /opt/DirectRM/scripts/

# Default command - show help
CMD ["python", "/opt/DirectRM/scripts/inference.py", "--help"]
