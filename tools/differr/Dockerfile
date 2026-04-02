ARG VERSION=0.2

FROM python:3.9-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# Install build tools + R with updated Matrix + compile differr
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    git \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    libwebp-dev \
    r-base \
    r-base-dev \
    ca-certificates && \
    # Update Matrix package to >= 1.5.0
    Rscript -e "install.packages('Matrix', repos='https://cloud.r-project.org/')" && \
    pip install --no-cache-dir \
    git+https://github.com/bartongroup/differr_nanopore_DRS.git@${VERSION} && \
    apt-get purge -y --auto-remove \
    gcc \
    g++ \
    git \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    r-base-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

# Smoke-test
RUN differr --help

WORKDIR /data

CMD ["differr", "--help"]
