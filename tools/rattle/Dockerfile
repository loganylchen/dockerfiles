ARG VERSION=1.0

FROM ubuntu:20.04 AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        ca-certificates \
        zlib1g-dev \
    && git clone --recurse-submodules --depth 1 --branch v${VERSION} \
        https://github.com/comprna/RATTLE /opt/RATTLE \
    && cd /opt/RATTLE \
    && (cd spoa && mkdir -p build && cd build && cmake -DCMAKE_BUILD_TYPE=Release .. && make) \
    && mkdir -p spoa/build/lib \
    && (cp spoa/build/libspoa.a spoa/build/lib/ 2>/dev/null || true) \
    && make \
    && strip rattle

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="RATTLE" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="RATTLE - reference-free reconstruction and quantification of transcriptomes from long-read sequencing" \
      org.opencontainers.image.source="https://github.com/comprna/RATTLE" \
      org.opencontainers.image.licenses="MIT"

RUN apt-get update && apt-get install -y --no-install-recommends \
        zlib1g \
        libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/RATTLE/rattle /usr/local/bin/rattle

RUN rattle --help > /dev/null 2>&1 || rattle 2>&1 | head -5

WORKDIR /data
CMD ["rattle"]
