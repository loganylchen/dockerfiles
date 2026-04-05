ARG VERSION=0.2.3

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
        install.packages(c('BiocManager', 'remotes'), repos='https://cloud.r-project.org/'); \
        remotes::install_github('rosedu1/deconvSeq', dependencies=TRUE) \
    " \
    && apt-get purge -y r-base-dev git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(deconvSeq); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
