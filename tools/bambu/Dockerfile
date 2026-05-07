ARG VERSION=3.14.0

# bambu 3.14.0 (Bioc 3.23) requires R 4.6. Older 3.8.x/3.10.x/3.12.x
# install fine on the same R 4.6 base since their Bioc deps maintain
# backward-compat APIs and we resolve deps from current Bioc 3.23.
FROM rocker/r-ver:4.6.0
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="bambu" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="bambu - context-aware transcript quantification from long-read RNA-seq data" \
      org.opencontainers.image.source="https://github.com/GoekeLab/bambu" \
      org.opencontainers.image.licenses="GPL-3.0"

# Map bambu version -> matching Bioconductor release that hosts that tarball.
# Only v3.12.1 has a GitHub tag; older bambu versions live only on Bioconductor.
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
    && case "${VERSION}" in \
         3.14.*) BIOC=3.23 ;; \
         3.12.*) BIOC=3.22 ;; \
         3.10.*) BIOC=3.21 ;; \
         3.8.*)  BIOC=3.20 ;; \
         3.6.*)  BIOC=3.19 ;; \
         3.4.*)  BIOC=3.18 ;; \
         *)      BIOC=3.23 ;; \
       esac \
    && BAMBU_URL="https://bioconductor.org/packages/${BIOC}/bioc/src/contrib/bambu_${VERSION}.tar.gz" \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        install.packages('remotes', repos='https://cloud.r-project.org/'); \
        install.packages(c('xgboost','optparse'), repos='https://cloud.r-project.org/'); \
        BiocManager::install(c( \
            'BiocGenerics','BiocParallel','BSgenome','data.table','dplyr','DESeq2', \
            'GenomicAlignments','GenomicFeatures','GenomicRanges','IRanges', \
            'Rsamtools','S4Vectors','SummarizedExperiment','tidyr','methods', \
            'rtracklayer','txdbmaker' \
        ), ask=FALSE, update=FALSE); \
        install.packages('${BAMBU_URL}', repos=NULL, type='source') \
    " \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(bambu); library(optparse); library(xgboost); \
        cat('bambu', as.character(packageVersion('bambu')), '\n'); \
        cat('xgboost', as.character(packageVersion('xgboost')), '\n'); \
        xgb.set.config(nthread = 1); cat('xgb.set.config OK\n'); \
        sessionInfo()" 2>&1 | head -25

WORKDIR /data
CMD ["Rscript"]
