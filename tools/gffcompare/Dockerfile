ARG VERSION=0.12.9

FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        build-essential \
        zlib1g-dev \
    && wget -q https://github.com/gpertea/gffcompare/archive/refs/tags/v${VERSION}.tar.gz \
        -O /tmp/gffcompare.tar.gz \
    && tar -xzf /tmp/gffcompare.tar.gz -C /tmp \
    && cd /tmp/gffcompare-${VERSION} \
    && make release \
    && strip gffcompare trmap \
    && mv gffcompare trmap /usr/local/bin/ \
    && rm -rf /var/lib/apt/lists/* /tmp/*

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

COPY --from=builder /usr/local/bin/gffcompare /usr/local/bin/gffcompare
COPY --from=builder /usr/local/bin/trmap /usr/local/bin/trmap

RUN gffcompare --version

WORKDIR /data
CMD ["gffcompare"]
