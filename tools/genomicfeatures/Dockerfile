ARG VERSION=1.62.0

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
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('GenomicFeatures', 'rtracklayer'), ask=FALSE) \
    " \
    && apt-get purge -y r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(GenomicFeatures); library(rtracklayer); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
