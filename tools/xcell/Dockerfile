ARG VERSION=1.1.0

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
        libgit2-dev \
        git \
        ca-certificates \
    && Rscript -e " \
        install.packages(c('BiocManager', 'devtools'), repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('GSEABase', 'GSVA'), ask=FALSE); \
        devtools::install_github('dviraran/xCell') \
    " \
    && apt-get purge -y --auto-remove r-base-dev git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(xCell); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
