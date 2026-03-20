ARG VERSION=1.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        zlib1g-dev \
        libfontconfig1-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libgit2-dev \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c( \
            'immunedeconv','GSVA','singscore','ComplexHeatmap'), ask=FALSE); \
        install.packages(c( \
            'pheatmap','ggplot2','reshape2','RColorBrewer', \
            'gridExtra','corrplot','circlize','ggpubr', \
            'tidyverse','scales','viridis'), \
            repos='https://cloud.r-project.org/') \
    " \
    && apt-get purge -y --auto-remove r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

# estimate is not on CRAN; install from r-universe
RUN Rscript -e " \
    install.packages('estimate', \
        repos='https://bu-cnio.r-universe.dev') \
"

RUN Rscript -e "library(immunedeconv); library(estimate); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
