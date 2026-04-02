ARG VERSION=2.3

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        unzip \
        openjdk-17-jre-headless \
        perl \
        python3 \
        libgomp1 \
        fontconfig \
    && wget -q https://bitbucket.org/kokonech/qualimap/downloads/qualimap_v${VERSION}.zip \
        -O /tmp/qualimap.zip \
    && unzip /tmp/qualimap.zip -d /opt \
    && mv /opt/qualimap_v${VERSION} /opt/qualimap \
    && chmod +x /opt/qualimap/qualimap \
    && ln -s /opt/qualimap/qualimap /usr/local/bin/qualimap \
    && apt-get purge -y wget ca-certificates unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN qualimap --help 2>&1

WORKDIR /data
CMD ["qualimap"]
