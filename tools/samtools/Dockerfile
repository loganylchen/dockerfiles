ARG SAMTOOLS_VERSION=1.21
ARG BCFTOOLS_VERSION=1.21
ARG HTSLIB_VERSION=1.21

# Build stage
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG SAMTOOLS_VERSION
ARG BCFTOOLS_VERSION
ARG HTSLIB_VERSION

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libncurses-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libdeflate-dev \
        autoconf \
        automake \
        bzip2 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/build

# Build htslib first (required by samtools and bcftools)
RUN curl -L https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/htslib-${HTSLIB_VERSION}.tar.bz2 | tar -jxf - && \
    cd htslib-${HTSLIB_VERSION} && \
    ./configure --prefix=/usr/local --enable-libcurl --enable-plugins && \
    make -j$(nproc) && \
    make install && \
    ldconfig

# Build samtools
RUN curl -L https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 | tar -jxf - && \
    cd samtools-${SAMTOOLS_VERSION} && \
    ./configure --prefix=/usr/local --with-htslib=/usr/local --without-curses && \
    make -j$(nproc) && \
    make install && \
    strip /usr/local/bin/samtools

# Build bcftools
RUN curl -L https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2 | tar -jxf - && \
    cd bcftools-${BCFTOOLS_VERSION} && \
    ./configure --prefix=/usr/local --with-htslib=/usr/local && \
    make -j$(nproc) && \
    make install && \
    strip /usr/local/bin/bcftools

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/loganylchen/dockerfiles"
LABEL org.opencontainers.image.description="Samtools and BCFtools for BAM/VCF manipulation"
LABEL org.opencontainers.image.licenses="MIT"

ARG SAMTOOLS_VERSION
ARG BCFTOOLS_VERSION
ARG HTSLIB_VERSION

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        zlib1g \
        libbz2-1.0 \
        liblzma5 \
        libcurl4 \
        libssl3 \
        libdeflate0 \
        perl \
        && rm -rf /var/lib/apt/lists/* \
        && apt-get clean

# Copy binaries and libraries from builder
COPY --from=builder /usr/local/bin/samtools /usr/local/bin/
COPY --from=builder /usr/local/bin/bcftools /usr/local/bin/
COPY --from=builder /usr/local/lib/libhts* /usr/local/lib/
COPY --from=builder /usr/local/lib/pkgconfig /usr/local/lib/pkgconfig
COPY --from=builder /usr/local/include/htslib /usr/local/include/htslib

# Update library cache
RUN ldconfig

# Create working directory
WORKDIR /data

# Verify installations
RUN samtools --version && bcftools --version

# Default command
CMD ["samtools"]
