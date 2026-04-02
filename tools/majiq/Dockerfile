ARG VERSION=2.4.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        libhts-dev \
        zlib1g-dev \
        wget \
        ca-certificates \
    && pip3 install --no-cache-dir --break-system-packages \
        majiq==${VERSION} \
    && apt-get purge -y --auto-remove python3-dev gcc wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN majiq --version

WORKDIR /data
CMD ["majiq"]
