# Build stage
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION=2.28

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
        autoconf \
        automake && \
    rm -rf /var/lib/apt/lists/*

# Build minimap2 from source
WORKDIR /tmp
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${VERSION}/minimap2-${VERSION}.tar.bz2 | tar -jxf - && \
    cd minimap2-${VERSION} && \
    make && \
    strip minimap2

# Build samtools from source
RUN curl -L https://github.com/samtools/samtools/releases/download/1.19.2/samtools-1.19.2.tar.bz2 | tar -jxf - && \
    cd samtools-1.19.2 && \
    ./configure --without-curses && \
    make && \
    strip samtools

# Download k8 precompiled binary
RUN curl -L https://github.com/attractivechaos/k8/releases/download/v1.2/k8-1.2.tar.bz2 | tar -jxf -

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION=2.28

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        zlib1g \
        libbz2-1.0 \
        liblzma5 \
        libncurses6 && \
    rm -rf /var/lib/apt/lists/*

# Copy binaries from builder
COPY --from=builder /tmp/minimap2-*/minimap2 /usr/local/bin/
COPY --from=builder /tmp/samtools-*/samtools /usr/local/bin/
COPY --from=builder /tmp/k8-*/k8-x86_64-Linux /usr/local/bin/k8

# Copy JavaScript utilities from minimap2
COPY --from=builder /tmp/minimap2-*/misc/*.js /usr/local/share/minimap2/

# Make k8 executable and create wrapper scripts
RUN chmod +x /usr/local/bin/k8 && \
    echo '#!/bin/sh' > /usr/local/bin/paftools.js && \
    echo 'exec k8 /usr/local/share/minimap2/paftools.js "$@"' >> /usr/local/bin/paftools.js && \
    chmod +x /usr/local/bin/paftools.js && \
    echo '#!/bin/sh' > /usr/local/bin/pafcluster.js && \
    echo 'exec k8 /usr/local/share/minimap2/pafcluster.js "$@"' >> /usr/local/bin/pafcluster.js && \
    chmod +x /usr/local/bin/pafcluster.js

# Verify installations
RUN minimap2 --version && \
    samtools --version && \
    k8 -v && \
    ls -la /usr/local/share/minimap2/

WORKDIR /data

CMD ["minimap2"]

