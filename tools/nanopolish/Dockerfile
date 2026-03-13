# Build stage
FROM debian:bookworm-slim AS builder

ARG VERSION=0.14.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates \
        git \
        autoconf \
        automake \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        libhdf5-dev && \
    rm -rf /var/lib/apt/lists/*

# Clone nanopolish with all submodules at the specified tag
WORKDIR /tmp
RUN git clone --recursive --depth=1 --branch v${VERSION} \
        https://github.com/jts/nanopolish.git && \
    cd nanopolish && \
    git submodule update --init --recursive && \
    make HDF5=noinstall && \
    strip nanopolish

# Runtime stage
FROM debian:bookworm-slim

# Only runtime shared libs needed by the nanopolish binary
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libhdf5-103-1 \
        zlib1g \
        libbz2-1.0 \
        liblzma5 \
        libcurl4 \
        libssl3 \
        python3 \
        python3-pip \
        ca-certificates && \
    pip3 install --no-cache-dir --break-system-packages \
        numpy \
        scipy \
        pysam \
        biopython && \
    rm -rf /var/lib/apt/lists/*

# Copy nanopolish binary and helper scripts from builder
COPY --from=builder /tmp/nanopolish/nanopolish /usr/local/bin/nanopolish
COPY --from=builder /tmp/nanopolish/scripts /usr/local/share/nanopolish/scripts

RUN ln -sf /usr/local/share/nanopolish/scripts/nanopolish_makerange.py /usr/local/bin/nanopolish_makerange.py && \
    chmod +x /usr/local/bin/nanopolish_makerange.py

# Smoke-test
RUN nanopolish --version

WORKDIR /data

CMD ["nanopolish", "--help"]
