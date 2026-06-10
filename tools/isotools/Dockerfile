ARG VERSION=0.3.4

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="IsoTools" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="IsoTools - framework for the analysis of long read transcriptome sequencing data" \
      org.opencontainers.image.source="https://github.com/MatthiasLienhard/isotools" \
      org.opencontainers.image.licenses="MIT"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        python-is-python3 \
        gcc \
        g++ \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-openssl-dev \
        libssl-dev \
    && pip3 install --no-cache-dir --break-system-packages \
        'numpy<2' \
        "isotools==${VERSION}" \
    && apt-get purge -y --auto-remove python3-dev gcc g++ zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

RUN python3 -c "import isotools; print('isotools', isotools.__version__)" \
    && python -c "import sys; print('python ->', sys.executable)" \
    && run_isotools --help > /dev/null

WORKDIR /data
CMD ["run_isotools"]
