# Multi-stage build for nanocompore - optimized for size
# Stage 1: Builder - Install build dependencies and compile
# Using Python 3.10 for compatibility with nanocompore's matplotlib dependencies
FROM python:3.10-slim AS builder

ARG VERSION=2.2.0

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    git \
    libhdf5-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment to isolate dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install nanocompore and its dependencies
# Install CPU-only PyTorch first to reduce image size (avoids CUDA dependencies)
# Install setuptools<58 to ensure pkg_resources is available (required by nanocompore)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir "setuptools<58" && \
    pip install --no-cache-dir nanocompore==${VERSION}

# Stage 2: Runtime - Minimal image with only runtime dependencies
FROM python:3.10-slim

ARG VERSION=2.2.0

LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="Nanocompore - RNA modification detection from Nanopore dRNA-Seq data"
LABEL version="${VERSION}"

# Install only runtime dependencies (no build tools)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libhdf5-310 \
    zlib1g \
    libbz2-1.0 \
    liblzma5 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set PATH to use virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /data

# Verify installation
RUN nanocompore --version && \
    python -c "import nanocompore; print(f'Nanocompore {nanocompore.__version__} installed successfully')"

# Default command
CMD ["nanocompore", "--help"]
