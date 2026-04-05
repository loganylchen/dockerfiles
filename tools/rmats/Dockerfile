ARG VERSION=4.3.0

FROM ubuntu:22.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV PATH=/opt/rmats:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc g++ gfortran \
        build-essential \
        ca-certificates \
        cmake \
        cython3 \
        git \
        libblas-dev \
        libgsl-dev \
        liblapack-dev \
        make \
        python-is-python3 \
        python3-dev \
        python3-pip \
        r-base \
        samtools \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && git clone --depth 1 --branch v${VERSION} \
        https://github.com/Xinglab/rmats-turbo.git /tmp/rmats \
    && cd /tmp/rmats \
    && echo '' > setup_environment.sh \
    && ./build_rmats \
    && mkdir -p /opt/rmats \
    && cp rmats.py cp_with_prefix.py *.so /opt/rmats/ \
    && mkdir -p /opt/rmats/rMATS_C && cp rMATS_C/rMATSexe /opt/rmats/rMATS_C/ \
    && mkdir -p /opt/rmats/rMATS_P && cp rMATS_P/*.py /opt/rmats/rMATS_P/ \
    && chmod -R +x /opt/rmats \
    && rm -rf /tmp/rmats

RUN rmats.py --help 2>&1 | head -5

WORKDIR /data
CMD ["rmats.py"]
