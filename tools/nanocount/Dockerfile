ARG VERSION=1.1.0.post2

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# Install build deps + runtime deps + NanoCount + purge build deps in one layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        gcc \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    pip3 install --no-cache-dir --break-system-packages \
        "tqdm>=4.51.0" \
        "numpy>=1.19.4" \
        "pysam>=0.16.0" \
        "pandas>=1.1.4" \
        "colorlog>=4.1.0" \
        "NanoCount==${VERSION}" && \
    apt-get purge -y --auto-remove \
        gcc \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Smoke test
RUN NanoCount --version

WORKDIR /data

CMD ["NanoCount"]
