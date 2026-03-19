ARG VERSION=2.31.1

FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        build-essential \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
    && wget -q https://github.com/arq5x/bedtools2/releases/download/v${VERSION}/bedtools-${VERSION}.tar.gz \
        -O /tmp/bedtools.tar.gz \
    && tar -xzf /tmp/bedtools.tar.gz -C /tmp \
    && cd /tmp/bedtools2 \
    && make -j$(nproc) \
    && strip bin/bedtools \
    && mv bin/bedtools /usr/local/bin/bedtools \
    && rm -rf /var/lib/apt/lists/* /tmp/*

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/bedtools /usr/local/bin/bedtools

RUN bedtools --version

WORKDIR /data
CMD ["bedtools"]
