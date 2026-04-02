ARG VERSION=1.26.0

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
        default-jdk \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('DEXSeq', 'BiocParallel', 'Rsamtools'), ask=FALSE); \
        install.packages( \
            c('https://bioconductor.org/packages/3.14/bioc/src/contrib/QoRTs_1.3.6.tar.gz', \
              'https://bioconductor.org/packages/3.14/bioc/src/contrib/JunctionSeq_${VERSION}.tar.gz'), \
            repos=NULL, type='source') \
    " \
    && apt-get purge -y --auto-remove r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(JunctionSeq); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
