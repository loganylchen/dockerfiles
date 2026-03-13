ARG VERSION=0.0.0.9000

FROM debian:bookworm-slim

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
        libgit2-dev \
    && Rscript -e " \
        install.packages(c( \
            'pheatmap','ggplot2','reshape2','RColorBrewer', \
            'dplyr','devtools','tidyverse'), \
            repos='https://cloud.r-project.org/'); \
        devtools::install_github('KaiAragaki/tidy_estimate@v${VERSION}') \
    " \
    && apt-get purge -y --auto-remove r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(tidyestimate); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
