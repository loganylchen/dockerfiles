ARG VERSION=4.2.1

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
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install('edgeR', ask=FALSE); \
        install.packages('dplyr', repos='https://cloud.r-project.org/') \
    " \
    && apt-get purge -y --auto-remove r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(edgeR); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
