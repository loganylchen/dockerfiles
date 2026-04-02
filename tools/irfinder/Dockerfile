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
        libhts-dev \
        python3 \
        bedtools \
        perl \
        default-jre \
        pigz \
        gzip \
    && wget -q https://github.com/RitchieLabIGH/IRFinder/archive/refs/tags/v${VERSION}.tar.gz \
        -O /tmp/irfinder.tar.gz \
    && tar -xzf /tmp/irfinder.tar.gz -C /opt \
    && cd /opt/IRFinder-${VERSION} \
    && make -j$(nproc) || true \
    && ln -s /opt/IRFinder-${VERSION}/bin/irfinder /usr/local/bin/irfinder \
    && chmod +x /opt/IRFinder-${VERSION}/bin/* \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('DESeq2'), ask=FALSE) \
    " \
    && apt-get purge -y --auto-remove wget ca-certificates r-base-dev build-essential \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

WORKDIR /data
CMD ["irfinder"]
