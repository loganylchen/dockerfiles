# Multi-stage build for slow5tools
# Stage 1: Builder
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION
ENV DEBIAN_FRONTEND=noninteractive
ENV ONT_VBZ_VERSION=v1.0.1
ENV ARCH=x86_64
ENV ONT_VBZ_FILE=ont-vbz-hdf-plugin-1.0.1-Linux-${ARCH}.tar.gz

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        wget \
        tar \
        gcc \
        g++ \
        make \
        autoconf \
        automake \
        libhdf5-dev \
        zlib1g-dev \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Download and install ONT VBZ plugin
RUN wget -q https://github.com/nanoporetech/vbz_compression/releases/download/$ONT_VBZ_VERSION/$ONT_VBZ_FILE -O /tmp/$ONT_VBZ_FILE && \
    mkdir -p /tmp/ont_vbz_plugin && \
    tar -xzf /tmp/$ONT_VBZ_FILE -C /tmp/ont_vbz_plugin && \
    mkdir -p /usr/local/lib && \
    find /tmp/ont_vbz_plugin -name '*.so' -exec cp {} /usr/local/lib/ \; && \
    rm -rf /tmp/*

# Build slow5tools
WORKDIR /tmp
RUN git clone --recursive https://github.com/hasindu2008/slow5tools && \
    cd slow5tools && \
    git checkout v${VERSION} && \
    git submodule update --init --recursive && \
    autoreconf --install && \
    ./configure && \
    make

# Stage 2: Runtime
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV PATH=/opt/bin:$PATH
ENV PLUGIN_PATH=/usr/local/lib
ENV HDF5_PLUGIN_PATH=${PLUGIN_PATH}

# Install only runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libhdf5-103-1 \
        zlib1g && \
    rm -rf /var/lib/apt/lists/*

# Copy VBZ plugin and slow5tools binary from builder
COPY --from=builder /usr/local/lib/*.so /usr/local/lib/
COPY --from=builder /tmp/slow5tools/slow5tools /opt/bin/

# Verify installation
RUN slow5tools --version

CMD ["slow5tools"]
