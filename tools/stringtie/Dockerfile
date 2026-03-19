ARG VERSION=2.2.3

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
    && wget -q https://github.com/gpertea/stringtie/releases/download/v${VERSION}/stringtie-${VERSION}.Linux_x86_64.tar.gz \
        -O /tmp/stringtie.tar.gz \
    && tar -xzf /tmp/stringtie.tar.gz -C /tmp \
    && cp /tmp/stringtie-${VERSION}.Linux_x86_64/stringtie /usr/local/bin/stringtie \
    && chmod +x /usr/local/bin/stringtie \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN stringtie --version

WORKDIR /data
CMD ["stringtie"]
