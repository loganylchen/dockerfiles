ARG VERSION=3.12.1

# bambu 3.8+ targets recent Bioconductor releases that require R >= 4.4.
# debian:bookworm-slim only ships R 4.2, so use rocker/r-ver:4.5.0 (still
# Debian-based) to get a modern R + Bioc 3.22 dep set that works for the
# 3.8.x / 3.10.x / 3.12.x lines we build.
FROM rocker/r-ver:4.5.0
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="bambu" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="bambu - context-aware transcript quantification from long-read RNA-seq data" \
      org.opencontainers.image.source="https://github.com/GoekeLab/bambu" \
      org.opencontainers.image.licenses="GPL-3.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        zlib1g-dev \
        libfontconfig1-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
        git \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        install.packages('remotes', repos='https://cloud.r-project.org/'); \
        remotes::install_version('xgboost', version='1.7.8.1', repos='https://cloud.r-project.org/'); \
        install.packages('optparse', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c( \
            'BiocGenerics','BiocParallel','BSgenome','data.table','dplyr','DESeq2', \
            'GenomicAlignments','GenomicFeatures','GenomicRanges','IRanges', \
            'Rsamtools','S4Vectors','SummarizedExperiment','tidyr','methods', \
            'rtracklayer','txdbmaker' \
        ), ask=FALSE, update=FALSE); \
        remotes::install_github('GoekeLab/bambu', ref='v${VERSION}', upgrade='never') \
    " \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(bambu); library(optparse); cat('bambu', as.character(packageVersion('bambu')), '\n'); sessionInfo()" 2>&1 | head -20

WORKDIR /data
CMD ["Rscript"]
