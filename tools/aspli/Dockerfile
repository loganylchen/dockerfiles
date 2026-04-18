ARG VERSION=2.14.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="ASpli" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="Bioconductor ASpli - analysis of alternative splicing using RNA-seq" \
      org.opencontainers.image.source="https://bioconductor.org/packages/ASpli" \
      org.opencontainers.image.licenses="GPL-3.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        zlib1g-dev \
        libfontconfig1-dev \
        libuv1-dev \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('ASpli', 'GenomicFeatures'), ask=FALSE) \
    " \
    && apt-get purge -y r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(ASpli); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
