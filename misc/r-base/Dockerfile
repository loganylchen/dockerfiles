ARG VERSION=1.0

# rocker/r-ver is Ubuntu jammy based with Posit PPM preconfigured to serve
# precompiled CRAN/Bioconductor *binaries* for this R version, so heavy/fragile
# source builds (e.g. the devtools -> miniUI -> shiny -> bslib chain, plus the
# Bioconductor stack) install reliably without compilation.
FROM rocker/r-ver:4.4.3
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

ADD ./install_R_packages.R /tmp/

# System libraries required by a handful of packages (curl/xml/fonts/image/git2).
# rocker already ships build-essential; PPM binaries avoid most compilation, but
# these provide the runtime shared libs the packages link against.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libfontconfig1-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
        libgit2-dev \
        libmagick++-dev \
        zlib1g-dev \
        git \
    && rm -rf /var/lib/apt/lists/* \
    && Rscript /tmp/install_R_packages.R \
    && rm -rf /tmp/* /root/.cache

RUN Rscript -e "library(tidyverse); library(ComplexHeatmap); library(DESeq2); library(GenomicFeatures)" 2>&1 | head -3

WORKDIR /data
CMD ["R"]
