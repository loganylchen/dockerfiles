ARG VERSION=1.0.5

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
        libgit2-dev \
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
        install.packages(c('BiocManager', 'devtools'), repos='https://cloud.r-project.org/'); \
        devtools::install_github('cozygene/bisque') \
    " \
    && apt-get purge -y --auto-remove r-base-dev git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(BisqueRNA); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
