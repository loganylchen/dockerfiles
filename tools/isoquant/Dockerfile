ARG VERSION=3.13.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="IsoQuant" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="IsoQuant - reference-based analysis and quantification of long RNA reads (Nanopore/PacBio)" \
      org.opencontainers.image.source="https://github.com/ablab/IsoQuant" \
      org.opencontainers.image.licenses="GPL-2.0-only"

# Runtime: minimap2 + samtools for alignment step in the IsoQuant pipeline
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        g++ \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        minimap2 \
        samtools \
    && pip3 install --no-cache-dir --break-system-packages \
        "isoquant==${VERSION}" \
    && apt-get purge -y --auto-remove python3-dev gcc g++ zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

RUN python3 -c "import isoquant" \
    && isoquant --help > /dev/null \
    && minimap2 --version \
    && samtools --version | head -1

WORKDIR /data
CMD ["isoquant", "--help"]
