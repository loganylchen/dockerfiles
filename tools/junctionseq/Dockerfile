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
        wget \
        ca-certificates \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('DEXSeq', 'BiocParallel', 'Rsamtools'), ask=FALSE) \
    " \
    && wget -q https://hartleys.github.io/QoRTs/QoRTs_LATEST.tar.gz \
        -O /tmp/QoRTs.tar.gz \
    && wget -q https://hartleys.github.io/JunctionSeq/install/JunctionSeq_LATEST.tar.gz \
        -O /tmp/JunctionSeq.tar.gz \
    && Rscript -e " \
        install.packages('/tmp/QoRTs.tar.gz', repos=NULL, type='source'); \
        install.packages('/tmp/JunctionSeq.tar.gz', repos=NULL, type='source') \
    " \
    && apt-get purge -y --auto-remove r-base-dev wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(JunctionSeq); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
