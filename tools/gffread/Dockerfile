ARG VERSION=0.12.7

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="gffread" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="gffread - GFF/GTF utility for filtering, sorting, format conversion" \
      org.opencontainers.image.source="https://github.com/gpertea/gffread" \
      org.opencontainers.image.licenses="MIT"

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
    && wget -q https://github.com/gpertea/gffread/releases/download/v${VERSION}/gffread-${VERSION}.Linux_x86_64.tar.gz \
        -O /tmp/gffread.tar.gz \
    && tar -xzf /tmp/gffread.tar.gz -C /tmp \
    && mv /tmp/gffread-${VERSION}.Linux_x86_64/gffread /usr/local/bin/gffread \
    && chmod +x /usr/local/bin/gffread \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN gffread --version

WORKDIR /data
CMD ["gffread"]
