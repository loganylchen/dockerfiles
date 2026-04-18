ARG VERSION=0.12.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="FastQC" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="FastQC - quality control tool for high-throughput sequencing data" \
      org.opencontainers.image.source="https://www.bioinformatics.babraham.ac.uk/projects/fastqc/" \
      org.opencontainers.image.licenses="GPL-3.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        unzip \
        ca-certificates \
        openjdk-17-jre-headless \
        perl \
        fontconfig \
    && wget -q https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${VERSION}.zip \
        -O /tmp/fastqc.zip \
    && unzip -q /tmp/fastqc.zip -d /opt/ \
    && chmod +x /opt/FastQC/fastqc \
    && ln -s /opt/FastQC/fastqc /usr/local/bin/fastqc \
    && apt-get purge -y --auto-remove wget unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN fastqc --version

WORKDIR /data
CMD ["fastqc"]
