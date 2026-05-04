ARG VERSION=1.4

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="tailfindr" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="tailfindr - poly(A)/poly(T) tail length estimator for Oxford Nanopore RNA and DNA reads" \
      org.opencontainers.image.source="https://github.com/adnaniazi/tailfindr" \
      org.opencontainers.image.licenses="GPL-3.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libhdf5-dev \
        libgit2-dev \
        libfontconfig1-dev \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libuv1-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
    && Rscript -e " \
        install.packages(c('BiocManager', 'remotes'), repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('Biostrings', 'Rsamtools'), ask=FALSE, update=FALSE); \
        remotes::install_github('hadley/pryr', upgrade='never'); \
        remotes::install_github('bokeh/rbokeh', upgrade='never'); \
        remotes::install_github('adnaniazi/tailfindr', ref='v${VERSION}', upgrade='never'); \
        if (!requireNamespace('tailfindr', quietly=TRUE)) stop('tailfindr install failed') \
    " \
    && apt-get purge -y --auto-remove \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libgit2-dev \
        libfontconfig1-dev \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libuv1-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

RUN Rscript -e "library(tailfindr); cat('tailfindr OK\n')"

WORKDIR /data
CMD ["Rscript"]
