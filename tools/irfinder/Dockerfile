ARG VERSION=2.0.1
ARG STAR_VERSION=2.7.11b

FROM btrspg/star:${STAR_VERSION} AS star

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ARG STAR_VERSION

LABEL org.opencontainers.image.title="IRFinder" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="IRFinder - detection and analysis of intron retention from RNA-seq (bundled STAR ${STAR_VERSION})" \
      org.opencontainers.image.source="https://github.com/RitchieLabIGH/IRFinder" \
      org.opencontainers.image.licenses="MIT"

COPY --from=star /usr/local/bin/STAR /usr/local/bin/STAR

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
        libboost-iostreams-dev \
        python3 \
        bedtools \
        perl \
        gawk \
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
    && cd /opt/IRFinder-${VERSION}/src/trim && make -j$(nproc) trim \
    && cp trim /opt/IRFinder-${VERSION}/bin/util/trim \
    && cd /opt/IRFinder-${VERSION}/src/winflat && make winflat \
    && cp winflat /opt/IRFinder-${VERSION}/bin/util/winflat \
    && cd /opt/IRFinder-${VERSION}/src/irfinder/Release && make -j$(nproc) \
    && cp irfinder /opt/IRFinder-${VERSION}/bin/util/irfinder \
    && chmod -R a+x /opt/IRFinder-${VERSION}/bin \
    && cp -r /opt/IRFinder-${VERSION} /usr/local/IRFinder \
    && ln -s /usr/local/IRFinder/bin/IRFinder /usr/bin/IRFinder \
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('DESeq2'), ask=FALSE) \
    " \
    && apt-get purge -y wget ca-certificates r-base-dev build-essential \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN IRFinder 2>&1 || true
RUN STAR --version

WORKDIR /data
CMD ["IRFinder"]
