ARG VERSION=3.4.0

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
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        install.packages('remotes', repos='https://cloud.r-project.org/'); \
        remotes::install_version('xgboost', version='1.7.8.1', repos='https://cloud.r-project.org/'); \
        BiocManager::install('bambu', ask=FALSE) \
    " \
    && apt-get purge -y r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(bambu); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
