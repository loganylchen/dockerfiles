ARG VERSION=2.0.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        minimap2 \
        samtools \
    && pip3 install --no-cache-dir --break-system-packages \
        flair-brookslab==${VERSION} \
    && apt-get purge -y --auto-remove python3-dev gcc \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN flair --version

WORKDIR /data
CMD ["flair"]
