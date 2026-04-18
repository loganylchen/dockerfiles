ARG VERSION=0.12.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

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
