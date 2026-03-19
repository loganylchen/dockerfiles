ARG VERSION=0.12.7

FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        build-essential \
        zlib1g-dev \
    && wget -q https://github.com/gpertea/gffread/archive/refs/tags/v${VERSION}.tar.gz \
        -O /tmp/gffread.tar.gz \
    && tar -xzf /tmp/gffread.tar.gz -C /tmp \
    && cd /tmp/gffread-${VERSION} \
    && make release \
    && strip gffread \
    && mv gffread /usr/local/bin/gffread \
    && rm -rf /var/lib/apt/lists/* /tmp/*

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

COPY --from=builder /usr/local/bin/gffread /usr/local/bin/gffread

RUN gffread --version

WORKDIR /data
CMD ["gffread"]
