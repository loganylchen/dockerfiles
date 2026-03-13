# Multi-stage build for nanocompore 1.x - optimized for size
# Note: Nanocompore 1.x requires Python 3.8 (PyYAML 5.x build fails on Python 3.10+)
# Nanocompore 2.x uses the separate nanocompore image (requires Python 3.10+)
FROM python:3.8-slim AS builder

ARG VERSION=1.0.4

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

# Install nanocompore 1.x and its dependencies (no PyTorch required)
RUN pip install --no-cache-dir nanocompore==${VERSION}

# Stage 2: Runtime - Minimal image with only runtime dependencies
FROM python:3.8-slim

ARG VERSION=1.0.4

LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="Nanocompore 1.x - RNA modification detection from Nanopore dRNA-Seq data"
LABEL version="${VERSION}"

# Install only runtime dependencies (no build tools)
# python:3.8-slim is based on Debian Buster, HDF5 package is libhdf5-103-1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libhdf5-103-1 \
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
