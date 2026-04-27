ARG VERSION=1.26.0

FROM rocker/r-ver:3.4.1
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="JunctionSeq" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="JunctionSeq 1.26.0 on R 3.4.1 / Bioconductor 3.5 (DESeq2 1.16.1)" \
      org.opencontainers.image.source="https://hartleys.github.io/JunctionSeq/" \
      org.opencontainers.image.licenses="GPL-3.0"

# rocker/r-ver:3.4.1 is debian stretch-based; stretch is archived.
# Pin CRAN to a 2017 PPM snapshot so dep versions stay compatible with Bioc 3.5.
RUN printf '%s\n' \
        'deb http://archive.debian.org/debian stretch main' \
        'deb http://archive.debian.org/debian-security stretch/updates main' \
        > /etc/apt/sources.list \
    && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid \
    && apt-get update && apt-get install -y --no-install-recommends \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        zlib1g-dev \
        libfontconfig1-dev \
        default-jdk \
        python3 \
        wget \
        ca-certificates \
    && Rscript -e " \
        options(download.file.method='wget', timeout=600, \
                repos=c( \
                    BioCsoft='https://bioconductor.org/packages/3.5/bioc', \
                    BioCann='https://bioconductor.org/packages/3.5/data/annotation', \
                    BioCexp='https://bioconductor.org/packages/3.5/data/experiment', \
                    CRAN='https://packagemanager.posit.co/cran/2017-10-31')); \
        install.packages(c('DESeq2', 'DEXSeq', 'BiocParallel', 'Rsamtools', \
                           'SummarizedExperiment', 'genefilter', 'geneplotter', \
                           'IRanges', 'GenomicRanges'), \
                         dependencies=TRUE); \
        stopifnot(packageVersion('DESeq2') == '1.16.1') \
    " \
    && wget -q https://hartleys.github.io/QoRTs/QoRTs_LATEST.tar.gz \
        -O /tmp/QoRTs.tar.gz \
    && wget -q https://hartleys.github.io/JunctionSeq/install/JunctionSeq_LATEST.tar.gz \
        -O /tmp/JunctionSeq.tar.gz \
    && mkdir -p /opt/QoRTs \
    && wget -q https://hartleys.github.io/QoRTs/QoRTs.jar \
        -O /opt/QoRTs/QoRTs.jar \
    && Rscript -e " \
        options(download.file.method='wget', timeout=600, \
                repos=c(CRAN='https://packagemanager.posit.co/cran/2017-10-31')); \
        install.packages(c('Hmisc', 'plotrix')); \
        install.packages('/tmp/QoRTs.tar.gz', repos=NULL, type='source'); \
        install.packages('/tmp/JunctionSeq.tar.gz', repos=NULL, type='source'); \
        java_dir <- file.path(find.package('QoRTs'), 'java'); \
        dir.create(java_dir, recursive=TRUE, showWarnings=FALSE); \
        stopifnot(file.copy('/opt/QoRTs/QoRTs.jar', \
                            file.path(java_dir, 'QoRTs.jar'), \
                            overwrite=TRUE)) \
    " \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

ENV QORTS_JAR=/opt/QoRTs/QoRTs.jar

RUN Rscript -e " \
        library(JunctionSeq); \
        cat('DESeq2:', as.character(packageVersion('DESeq2')), '\n'); \
        cat('JunctionSeq:', as.character(packageVersion('JunctionSeq')), '\n'); \
        stopifnot(packageVersion('DESeq2') == '1.16.1') \
    " \
    && Rscript -e " \
        jar <- system.file('java', 'QoRTs.jar', package='QoRTs'); \
        cat('QoRTs.jar:', jar, '\n'); \
        stopifnot(nzchar(jar), file.exists(jar)) \
    " \
    && test -f "$QORTS_JAR"

WORKDIR /data
CMD ["Rscript"]
