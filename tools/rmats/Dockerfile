ARG VERSION=4.3.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        g++ \
        gfortran \
        libgomp1 \
        libgsl-dev \
        cmake \
        git \
        ca-certificates \
        samtools \
    && pip3 install --no-cache-dir --break-system-packages \
        Cython numpy scipy \
    && git clone --depth 1 --branch v${VERSION} \
        https://github.com/Xinglab/rmats-turbo.git /tmp/rmats \
    && cd /tmp/rmats \
    && python3 setup.py build \
    && python3 setup.py install \
    && apt-get purge -y --auto-remove python3-dev gcc g++ gfortran cmake git ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN rmats.py --version

WORKDIR /data
CMD ["rmats.py"]
