ARG VERSION=4.1_8

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
    && Rscript -e " \
        install.packages(c( \
            'glmnet','pheatmap','ggplot2','reshape2','pROC', \
            'dplyr','prroc','timeROC','survminer','readr','tidyr', \
            'caret','ggsci'), repos='https://cloud.r-project.org/') \
    " \
    && apt-get purge -y r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(glmnet); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
