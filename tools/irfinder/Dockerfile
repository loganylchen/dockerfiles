ARG VERSION=2.0.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        samtools \
        r-base \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        build-essential \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        python3 \
        bedtools \
        perl \
        default-jre \
        pigz \
        gzip \
    && wget -q https://github.com/samtools/htslib/releases/download/1.21/htslib-1.21.tar.bz2 \
        -O /tmp/htslib.tar.bz2 \
    && tar -xjf /tmp/htslib.tar.bz2 -C /tmp \
    && cd /tmp/htslib-1.21 && make -j$(nproc) && make install \
    && ldconfig \
    && wget -q https://github.com/RitchieLabIGH/IRFinder/archive/refs/tags/v${VERSION}.tar.gz \
        -O /tmp/irfinder.tar.gz \
    && tar -xzf /tmp/irfinder.tar.gz -C /opt \
    && cd /opt/IRFinder-${VERSION} \
    && PKG_CONFIG_PATH=/usr/local/lib/pkgconfig make -j$(nproc) \
    && find /opt/IRFinder-${VERSION}/bin -type f -exec chmod +x {} \; \
    && ln -s "$(find /opt/IRFinder-${VERSION}/bin -type f | head -1)" /usr/local/bin/irfinder \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('DESeq2'), ask=FALSE) \
    " \
    && apt-get purge -y --auto-remove wget ca-certificates r-base-dev build-essential \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN irfinder --version 2>&1 || irfinder 2>&1 || true

WORKDIR /data
CMD ["irfinder"]
