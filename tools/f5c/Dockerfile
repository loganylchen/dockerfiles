ARG VERSION=1.6
FROM debian:bookworm-slim AS builder

ARG VERSION
WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    tar \
    bzip2 \
    gcc \
    g++ \
    make \
    cmake \
    autoconf \
    automake \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libhdf5-dev \
    libcurl4-openssl-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download and install prebuilt ONT VBZ plugin (if needed by f5c)
ENV ONT_VBZ_VERSION=v1.0.1
ENV ARCH=x86_64
ENV ONT_VBZ_FILE=ont-vbz-hdf-plugin-1.0.1-Linux-${ARCH}.tar.gz
RUN wget -q https://github.com/nanoporetech/vbz_compression/releases/download/$ONT_VBZ_VERSION/$ONT_VBZ_FILE -O /tmp/$ONT_VBZ_FILE && \
    mkdir -p /tmp/ont_vbz_plugin && \
    tar -xzf /tmp/$ONT_VBZ_FILE -C /tmp/ont_vbz_plugin && \
    mkdir -p /usr/local/lib/hdf5/plugin && \
    find /tmp/ont_vbz_plugin -name '*.so' -exec cp {} /usr/local/lib/hdf5/plugin/ \; && \
    rm -rf /tmp/*

# Download and build f5c
RUN wget https://github.com/hasindu2008/f5c/releases/download/v${VERSION}/f5c-v${VERSION}-release.tar.gz && \
    tar -xzf f5c-v${VERSION}-release.tar.gz && \
    cd f5c-v${VERSION} && \
    # Run the install script which downloads and builds htslib locally
    ./scripts/install-hts.sh && \
    autoreconf -i && \
    ./configure && \
    make -j$(nproc) && \
    cd ..

# Runtime stage
FROM debian:bookworm-slim

ARG VERSION
LABEL maintainer="Your Name <your.email@example.com>"
LABEL version="${VERSION}"
LABEL description="f5c - an optimised re-implementation of the call-methylation and eventalign modules in Nanopolish"

# Install runtime dependencies only
RUN apt-get update && apt-get install -y \
    libhdf5-103-1 \
    zlib1g \
    libbz2-1.0 \
    liblzma5 \
    bzip2 \
    && rm -rf /var/lib/apt/lists/*

# Create plugin directory
RUN mkdir -p /usr/local/lib/hdf5/plugin

# Copy built binaries from builder (f5c statically links htslib)
COPY --from=builder /build/f5c-v${VERSION}/f5c /usr/local/bin/
COPY --from=builder /usr/local/lib/hdf5/plugin/*.so /usr/local/lib/hdf5/plugin/

# Update library cache
RUN ldconfig

# Set HDF5 plugin path
ENV HDF5_PLUGIN_PATH=/usr/local/lib/hdf5/plugin

# Verify installation
RUN f5c --version

WORKDIR /data

# Default command
CMD ["f5c", "--help"]
