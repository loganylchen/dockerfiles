ARG VERSION=1.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

ADD ./install_R_packages.R /tmp/

RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
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
        zlib1g-dev \
        make \
        git \
    && rm -rf /var/lib/apt/lists/* \
    && Rscript -e " \
        install.packages(c( \
            'BiocManager', \
            'tidyverse', \
            'ggplot2', \
            'ggpubr', \
            'ggsci', \
            'ggrepel', \
            'ggalt', \
            'ggplotify', \
            'patchwork', \
            'pheatmap', \
            'UpSetR', \
            'dplyr', \
            'tidyr', \
            'tibble', \
            'readr', \
            'devtools', \
            'magick' \
        ), repos='https://cloud.r-project.org/') \
    " \
    && Rscript -e " \
        BiocManager::install(c( \
            'ComplexHeatmap', \
            'EnhancedVolcano', \
            'PCAtools', \
            'DESeq2' \
        ), ask=FALSE) \
    " \
    && Rscript /tmp/install_R_packages.R \
    && apt-get purge -y --auto-remove r-base-dev make git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(tidyverse); library(ComplexHeatmap); library(DESeq2)" 2>&1 | head -3

WORKDIR /data
CMD ["R"]
