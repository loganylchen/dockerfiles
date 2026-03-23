ARG VERSION=0.12.10

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
    && wget -q https://github.com/gpertea/gffcompare/releases/download/v${VERSION}/gffcompare-${VERSION}.Linux_x86_64.tar.gz \
        -O /tmp/gffcompare.tar.gz \
    && tar -xzf /tmp/gffcompare.tar.gz -C /tmp \
    && mv /tmp/gffcompare-${VERSION}.Linux_x86_64/gffcompare /usr/local/bin/gffcompare \
    && mv /tmp/gffcompare-${VERSION}.Linux_x86_64/trmap /usr/local/bin/trmap \
    && chmod +x /usr/local/bin/gffcompare /usr/local/bin/trmap \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN gffcompare --version

WORKDIR /data
CMD ["gffcompare"]
