ARG VERSION=2.4.2

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        openjdk-17-jre-headless \
        python3 \
    && wget -q https://github.com/getzlab/rnaseqc/releases/download/v${VERSION}/rnaseqc.v${VERSION}.linux.gz \
        -O /tmp/rnaseqc.gz \
    && gunzip /tmp/rnaseqc.gz \
    && mv /tmp/rnaseqc /usr/local/bin/rnaseqc \
    && chmod +x /usr/local/bin/rnaseqc \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN rnaseqc --version

WORKDIR /data
CMD ["rnaseqc"]
