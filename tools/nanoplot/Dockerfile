ARG VERSION=1.42.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="NanoPlot" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="NanoPlot - plotting suite for Oxford Nanopore sequencing data and alignments" \
      org.opencontainers.image.source="https://github.com/wdecoster/NanoPlot" \
      org.opencontainers.image.licenses="MIT"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-openssl-dev \
        libssl-dev \
    # NanoPlot 1.42.0 (2023-10-29) only declares lower bounds (plotly>=5.4.0,
    # pandas>=1.1.0, numpy>=1.16.5, kaleido). It was never tested against the
    # 2025+ majors which broke things:
    #   - plotly 6.x   : breaking changes vs the 5.x API NanoPlot uses
    #   - pandas 3.x   : removed several deprecated APIs
    #   - numpy 2.x    : ABI break for compiled deps (pysam, etc.)
    #   - kaleido 1.x  : dropped bundled binary, requires chromium browser
    # Pin to the last-known-tested ranges:
    && pip3 install --no-cache-dir --break-system-packages \
        'numpy<2' \
        'pandas>=2,<3' \
        'plotly>=5.4,<6' \
        'kaleido<1.0' \
        "NanoPlot==${VERSION}" \
    && apt-get purge -y --auto-remove python3-dev gcc zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

RUN NanoPlot --version

WORKDIR /data
CMD ["NanoPlot"]
