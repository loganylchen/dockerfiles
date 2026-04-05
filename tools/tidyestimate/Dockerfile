ARG VERSION=1.1.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

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
        libfreetype-dev \
        libpng-dev \
        libtiff-dev \
        libjpeg-dev \
        git \
        ca-certificates \
    && Rscript -e " \
        install.packages(c( \
            'pheatmap','ggplot2','reshape2','RColorBrewer', \
            'dplyr','remotes','tidyverse'), \
            repos='https://cloud.r-project.org/'); \
        remotes::install_github('KaiAragaki/tidy_estimate@v${VERSION}') \
    " \
    && apt-get purge -y r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(tidyestimate); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
