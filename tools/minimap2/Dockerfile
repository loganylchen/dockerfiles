# Build stage
FROM alpine:3.19 AS builder

ARG VERSION=2.28

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    curl \
    zlib-dev \
    bzip2-dev \
    xz-dev \
    ncurses-dev \
    autoconf \
    automake

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

# Runtime stage
FROM alpine:3.19

ARG VERSION=2.28

# Install runtime dependencies including k8 (JavaScript runtime)
RUN apk add --no-cache \
    zlib \
    libbz2 \
    xz-libs \
    ncurses-libs \
    libgcc \
    libstdc++ \
    curl

# Install k8 JavaScript shell for running paftools.js and other scripts
RUN curl -L https://github.com/attractivechaos/k8/releases/download/v1.2/k8-1.2.tar.bz2 | tar -jxf - && \
    mv k8-1.2/k8-* /usr/local/bin/k8 && \
    chmod +x /usr/local/bin/k8 && \
    rm -rf k8-1.2

# Copy binaries from builder
COPY --from=builder /tmp/minimap2-*/minimap2 /usr/local/bin/
COPY --from=builder /tmp/samtools-*/samtools /usr/local/bin/

# Copy JavaScript utilities from minimap2
COPY --from=builder /tmp/minimap2-*/misc/*.js /usr/local/share/minimap2/

# Create wrapper scripts for JavaScript tools
RUN echo '#!/bin/sh' > /usr/local/bin/paftools.js && \
    echo 'exec k8 /usr/local/share/minimap2/paftools.js "$@"' >> /usr/local/bin/paftools.js && \
    chmod +x /usr/local/bin/paftools.js && \
    echo '#!/bin/sh' > /usr/local/bin/pafcluster.js && \
    echo 'exec k8 /usr/local/share/minimap2/pafcluster.js "$@"' >> /usr/local/bin/pafcluster.js && \
    chmod +x /usr/local/bin/pafcluster.js

# Remove curl to minimize final image size
RUN apk del curl

# Verify installations
RUN minimap2 --version && \
    samtools --version && \
    k8 -v && \
    ls -la /usr/local/share/minimap2/

WORKDIR /data

CMD ["minimap2"]

