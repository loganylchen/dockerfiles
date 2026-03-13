ARG VERSION=0.23.4

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
    && wget -q https://github.com/OpenGene/fastp/releases/download/v${VERSION}/fastp \
        -O /usr/local/bin/fastp \
    && chmod +x /usr/local/bin/fastp \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN fastp --version 2>&1 | head -1

WORKDIR /data
CMD ["fastp"]
