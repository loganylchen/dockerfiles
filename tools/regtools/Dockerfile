ARG VERSION=1.0.0

# Builder stage: compile regtools with CMake
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        build-essential \
        cmake \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && wget -q https://github.com/griffithlab/regtools/archive/refs/tags/${VERSION}.tar.gz \
    && tar -xzf ${VERSION}.tar.gz \
    && cd regtools-${VERSION} \
    && mkdir build && cd build \
    && cmake .. \
    && make -j$(nproc) \
    && strip regtools

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        zlib1g \
        libbz2-1.0 \
        liblzma5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /tmp/regtools-*/build/regtools /usr/local/bin/regtools

RUN regtools --help

WORKDIR /data
CMD ["regtools"]
