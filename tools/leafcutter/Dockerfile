ARG VERSION=0.2.7

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
        libbz2-dev \
        liblzma-dev \
        libuv1-dev \
        libgit2-dev \
        python3 \
        wget \
        ca-certificates \
        samtools \
        git \
        build-essential \
        cmake \
    && wget -q https://github.com/samtools/htslib/releases/download/1.21/htslib-1.21.tar.bz2 -O /tmp/htslib.tar.bz2 \
    && tar -xjf /tmp/htslib.tar.bz2 -C /tmp \
    && cd /tmp/htslib-1.21 && make -j$(nproc) && make install \
    && ldconfig \
    && wget -q https://github.com/griffithlab/regtools/archive/refs/tags/1.0.0.tar.gz -O /tmp/regtools.tar.gz \
    && tar -xzf /tmp/regtools.tar.gz -C /tmp \
    && cd /tmp/regtools-1.0.0 && mkdir build && cd build \
    && cmake .. && make -j$(nproc) \
    && cp /tmp/regtools-1.0.0/build/regtools /usr/local/bin/ \
    && Rscript -e " \
        install.packages(c('remotes', 'optparse', 'rstan', 'rstantools', 'foreach', \
            'ggplot2', 'R.utils', 'gridExtra', 'reshape2', 'Hmisc', 'dplyr', 'doMC'), \
            repos='https://cloud.r-project.org/'); \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('Biobase', 'DirichletMultinomial'), ask=FALSE); \
        remotes::install_github('davidaknowles/leafcutter/leafcutter', ref='v${VERSION}') \
    " \
    && wget -q https://raw.githubusercontent.com/davidaknowles/leafcutter/v${VERSION}/scripts/leafcutter_ds.R \
        -O /usr/local/bin/leafcutter_ds.R \
    && chmod +x /usr/local/bin/leafcutter_ds.R \
    && wget -q https://raw.githubusercontent.com/davidaknowles/leafcutter/v${VERSION}/clustering/leafcutter_cluster_regtools.py \
        -O /usr/local/bin/leafcutter_cluster_regtools.py \
    && chmod +x /usr/local/bin/leafcutter_cluster_regtools.py \
    && apt-get purge -y --auto-remove r-base-dev wget ca-certificates git build-essential cmake \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN regtools --help 2>&1 || true

WORKDIR /data
CMD ["Rscript"]
