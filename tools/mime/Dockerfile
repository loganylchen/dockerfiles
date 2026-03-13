ARG VERSION=9a9f6ac89851bf631f9df3868b2fa624bed49df2

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
        libfontconfig1-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libgit2-dev \
        libprotobuf-dev \
        protobuf-compiler \
        cmake \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
        libsodium-dev \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c( \
            'GSVA','GSEABase','CancerClass','mixOmics','sparrow', \
            'sva','ComplexHeatmap'), ask=FALSE); \
        install.packages(c( \
            'klaR','devtools','survminer','xgboost','remotes'), \
            repos='https://cloud.r-project.org/') \
    " \
    && apt-get purge -y --auto-remove r-base-dev cmake \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

ADD ./install_R_packages.R /tmp/

RUN Rscript /tmp/install_R_packages.R ${VERSION}

WORKDIR /data
CMD ["R"]
