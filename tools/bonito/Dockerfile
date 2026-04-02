ARG VERSION=0.8.1
ARG CUDA_VERSION=12.3.1

FROM nvidia/cuda:${CUDA_VERSION}-devel-ubuntu22.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ARG CUDA_VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-dev \
        python3-pip \
        gcc \
        git \
        zlib1g-dev \
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir ont-bonito==${VERSION} \
    && apt-get purge -y --auto-remove git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN bonito --version

WORKDIR /data
CMD ["bonito"]
