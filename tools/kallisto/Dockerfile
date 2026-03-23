ARG VERSION=0.52.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        libstdc++6 \
    && wget -q https://github.com/pachterlab/kallisto/releases/download/v${VERSION}/kallisto_linux-v${VERSION}.tar.gz \
        -O /tmp/kallisto.tar.gz \
    && tar -xzf /tmp/kallisto.tar.gz -C /tmp \
    && cp /tmp/kallisto/kallisto /usr/local/bin/kallisto \
    && chmod +x /usr/local/bin/kallisto \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN kallisto version

WORKDIR /data
CMD ["kallisto"]
