ARG VERSION=1.0.13

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
    && Rscript -e " \
        install.packages(c( \
            'estimate','pheatmap','ggplot2','reshape2', \
            'RColorBrewer','dplyr'), repos='https://cloud.r-project.org/') \
    " \
    && apt-get purge -y --auto-remove r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(estimate); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
