ARG VERSION=2.4.2

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="FLAMES" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="FLAMES - Full-Length Analysis of Mutations and Splicing in long-read RNA-seq" \
      org.opencontainers.image.source="https://github.com/mritchielab/FLAMES" \
      org.opencontainers.image.licenses="GPL-3.0-or-later"

# FLAMES is a Bioconductor package (RELEASE_3_22 -> v2.4.2). It pulls in:
#   - bambu, BiocParallel, Biostrings, GenomicAlignments, ShortRead, Rsamtools,
#     scater, scran, ComplexHeatmap, ggbio, magick (image), ...
#   - Compiled deps via Rcpp + Rhtslib (htslib bundled in Rhtslib).
#   - basilisk + reticulate for the Python side (basilisk manages a private
#     conda env at first runtime call — not pre-warmed here).
# SystemRequirements: GNU make, C++17.
RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        build-essential \
        cmake \
        pkg-config \
        wget \
        ca-certificates \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libgit2-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libdeflate-dev \
        libpcre2-dev \
        libfontconfig1-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
        libcairo2-dev \
        libmagick++-dev \
        libgsl-dev \
        libudunits2-dev \
        libgdal-dev \
    && Rscript -e " \
        options(Ncpus = parallel::detectCores()); \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(version='3.22', ask=FALSE, update=FALSE); \
        BiocManager::install('FLAMES', ask=FALSE, update=FALSE) \
    " \
    && apt-get purge -y --auto-remove \
        r-base-dev build-essential cmake pkg-config wget \
        libcurl4-openssl-dev libssl-dev libxml2-dev libgit2-dev \
        zlib1g-dev libbz2-dev liblzma-dev libdeflate-dev libpcre2-dev \
        libfontconfig1-dev libharfbuzz-dev libfribidi-dev libfreetype6-dev \
        libpng-dev libtiff5-dev libjpeg-dev libcairo2-dev libmagick++-dev \
        libgsl-dev libudunits2-dev libgdal-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(FLAMES); cat('FLAMES', as.character(packageVersion('FLAMES')), '\n')" 2>&1 | tail -5

WORKDIR /data
CMD ["Rscript"]
