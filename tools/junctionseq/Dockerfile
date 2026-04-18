ARG VERSION=1.26.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="JunctionSeq" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="JunctionSeq - differential junction/exon usage analysis via QoRTs" \
      org.opencontainers.image.source="https://hartleys.github.io/JunctionSeq/" \
      org.opencontainers.image.licenses="GPL-3.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        zlib1g-dev \
        libfontconfig1-dev \
        default-jdk \
        libuv1-dev \
        python3 \
        wget \
        ca-certificates \
    && Rscript -e " \
        options(download.file.method='wget', timeout=600); \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install(c('DEXSeq', 'DESeq2', 'BiocParallel', 'Rsamtools', \
            'SummarizedExperiment', 'genefilter', 'geneplotter', \
            'IRanges', 'GenomicRanges'), ask=FALSE) \
    " \
    && wget -q https://hartleys.github.io/QoRTs/QoRTs_LATEST.tar.gz \
        -O /tmp/QoRTs.tar.gz \
    && wget -q https://hartleys.github.io/JunctionSeq/install/JunctionSeq_LATEST.tar.gz \
        -O /tmp/JunctionSeq.tar.gz \
    && mkdir -p /opt/QoRTs \
    && Rscript -e " \
        options(download.file.method='wget', timeout=600); \
        install.packages(c('Hmisc', 'plotrix'), repos='https://cloud.r-project.org/'); \
        install.packages('/tmp/QoRTs.tar.gz', repos=NULL, type='source'); \
        install.packages('/tmp/JunctionSeq.tar.gz', repos=NULL, type='source'); \
        jar <- system.file('extdata', 'QoRTs.jar', package='QoRTs'); \
        if (!nzchar(jar)) jar <- system.file('java', 'QoRTs.jar', package='QoRTs'); \
        if (!nzchar(jar) || !file.exists(jar)) stop('QoRTs.jar not found in installed package'); \
        java_dir <- file.path(find.package('QoRTs'), 'java'); \
        dir.create(java_dir, recursive=TRUE, showWarnings=FALSE); \
        stopifnot(file.copy(jar, file.path(java_dir, 'QoRTs.jar'), overwrite=TRUE)); \
        stopifnot(file.copy(jar, '/opt/QoRTs/QoRTs.jar', overwrite=TRUE)) \
    " \
    && apt-get purge -y r-base-dev \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

ENV QORTS_JAR=/opt/QoRTs/QoRTs.jar

RUN Rscript -e "library(JunctionSeq); sessionInfo()" 2>&1 \
    && Rscript -e "jar <- system.file('java', 'QoRTs.jar', package='QoRTs'); \
        cat('QoRTs.jar (java):', jar, '\n'); \
        stopifnot(nzchar(jar), file.exists(jar))" \
    && test -f "$QORTS_JAR"

WORKDIR /data
CMD ["Rscript"]
