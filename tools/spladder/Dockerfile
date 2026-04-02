ARG VERSION=3.0.4

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
    && pip3 install --no-cache-dir --break-system-packages \
        spladder==${VERSION} \
        'matplotlib<3.7' \
    && apt-get purge -y --auto-remove python3-dev gcc \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN spladder --help 2>&1 | head -3

WORKDIR /data
CMD ["spladder"]
