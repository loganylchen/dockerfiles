ARG VERSION=2.2.3

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
        git \
    && Rscript -e " \
        install.packages(c('BiocManager', 'devtools', 'snowfall', 'NMF'), repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('BiocParallel', 'scran'), ask=FALSE); \
        devtools::install_github('Danko-Lab/BayesPrism/BayesPrism') \
    " \
    && apt-get purge -y --auto-remove r-base-dev git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN Rscript -e "library(BayesPrism); sessionInfo()" 2>&1 | head -5

WORKDIR /data
CMD ["Rscript"]
