ARG VERSION=1.3.4

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="LIQA" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="LIQA - long-read isoform quantification and analysis" \
      org.opencontainers.image.source="https://github.com/WGLab/LIQA" \
      org.opencontainers.image.licenses="MIT"

# LIQA = Python (pysam, numpy, scipy, lifelines) + R (gcmr, betareg).
# gcmr depends on betareg + sandwich + Formula; all are CRAN.
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        g++ \
        gfortran \
        make \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        r-base \
        r-base-dev \
    && pip3 install --no-cache-dir --break-system-packages \
        "liqa==${VERSION}" \
    && Rscript -e " \
        install.packages(c('betareg','gcmr'), \
            repos='https://cloud.r-project.org/', \
            Ncpus=parallel::detectCores()) \
    " \
    && apt-get purge -y --auto-remove \
        python3-dev gcc g++ gfortran \
        zlib1g-dev libbz2-dev liblzma-dev \
        libcurl4-openssl-dev libssl-dev \
        r-base-dev \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

RUN python3 -c "import pysam, numpy, scipy, lifelines" \
    && Rscript -e "library(gcmr); library(betareg)" 2>&1 | tail -5 \
    && liqa 2>&1 | head -5 || true

WORKDIR /data
CMD ["liqa"]
