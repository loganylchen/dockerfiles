ARG VERSION=2.1

# Multi-stage build for xpore - optimized for size
# Stage 1: Builder - Install build dependencies and compile

FROM python:3.12-slim AS builder

ARG VERSION

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libhdf5-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment to isolate dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install xpore and its dependencies
# Note: xpore uses versioning like "v2.1", not "2.1"
# Pin numpy<2 to avoid compatibility warnings with PyArrow
RUN pip install --no-cache-dir "numpy<2" && \
    pip install --no-cache-dir xpore==v${VERSION}

# Stage 2: Runtime - Minimal image with only runtime dependencies
FROM python:3.12-slim

ARG VERSION

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="xPore - Identification of differential RNA modifications from direct RNA sequencing"
LABEL version="${VERSION}"

# Install only runtime dependencies (h5py 3.x+ bundles HDF5, no system lib needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    zlib1g \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set PATH to use virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /data

# Verify installation
RUN xpore --help && \
    python -c "import xpore; print('xPore installed successfully')"

# Default command
CMD ["xpore", "--help"]
