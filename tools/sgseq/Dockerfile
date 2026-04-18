ARG VERSION=1.38.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="SGSeq" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="SGSeq - analysis of splice events from RNA-seq data (Bioconductor)" \
      org.opencontainers.image.source="https://bioconductor.org/packages/SGSeq/" \
      org.opencontainers.image.licenses="Artistic-2.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        zlib1g-dev \
        libfontconfig1-dev \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('SGSeq', 'GenomicFeatures'), ask=FALSE) \
    " \
    && apt-get purge -y r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(SGSeq); sessionInfo()" 2>&1

WORKDIR /data
CMD ["Rscript"]
