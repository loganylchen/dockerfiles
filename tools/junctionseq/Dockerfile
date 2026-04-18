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
    && Rscript -e " \
        options(download.file.method='wget', timeout=600); \
        install.packages(c('Hmisc', 'plotrix'), repos='https://cloud.r-project.org/'); \
        install.packages('/tmp/QoRTs.tar.gz', repos=NULL, type='source'); \
        install.packages('/tmp/JunctionSeq.tar.gz', repos=NULL, type='source') \
    " \
    # Expose QoRTs.jar at stable paths so downstream scripts can locate it
    # via system.file("java", ...) or system.file("extdata", ...) or $QORTS_JAR.
    && QORTS_PKG_DIR="$(Rscript -e 'cat(find.package(\"QoRTs\"))')" \
    && QORTS_JAR_SRC="$(find \"$QORTS_PKG_DIR\" -name 'QoRTs.jar' | head -n1)" \
    && if [ -z "$QORTS_JAR_SRC" ]; then \
           mkdir -p /tmp/qortsrc \
           && tar -xzf /tmp/QoRTs.tar.gz -C /tmp/qortsrc \
           && QORTS_JAR_SRC="$(find /tmp/qortsrc -name 'QoRTs.jar' | head -n1)"; \
       fi \
    && mkdir -p "$QORTS_PKG_DIR/java" /opt/QoRTs \
    && cp "$QORTS_JAR_SRC" "$QORTS_PKG_DIR/java/QoRTs.jar" \
    && cp "$QORTS_JAR_SRC" /opt/QoRTs/QoRTs.jar \
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
