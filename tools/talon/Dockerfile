ARG VERSION=5.0

FROM python:3.7-slim-bullseye
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="TALON" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="TALON - technology-agnostic long read analysis pipeline for identifying known and novel genes/isoforms" \
      org.opencontainers.image.source="https://github.com/mortazavilab/TALON" \
      org.opencontainers.image.licenses="MIT"

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-openssl-dev \
        libssl-dev \
    && pip install --no-cache-dir \
        'numpy<1.22' \
        'pandas<1.4' \
        'pysam>=0.15.4' \
        pyfaidx \
        'bamread>=0.0.11' \
        pyranges \
        scanpy \
    && wget -q https://github.com/mortazavilab/TALON/archive/refs/tags/v${VERSION}.tar.gz -O /tmp/talon.tar.gz \
    && tar -xzf /tmp/talon.tar.gz -C /tmp \
    && cd /tmp/TALON-${VERSION} \
    && pip install --no-cache-dir . \
    && apt-get purge -y --auto-remove build-essential wget zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN talon --help > /dev/null && talon_label_reads --help > /dev/null \
    && python -c "import talon; print('talon OK')"

WORKDIR /data
CMD ["talon"]
