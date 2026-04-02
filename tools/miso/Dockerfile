ARG VERSION=0.5.4

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python2 \
        python2-dev \
        wget \
        ca-certificates \
        gcc \
        libc6-dev \
        samtools \
    && wget -q https://bootstrap.pypa.io/pip/2.7/get-pip.py -O /tmp/get-pip.py \
    && python2 /tmp/get-pip.py \
    && pip2 install --no-cache-dir \
        misopy==${VERSION} \
        numpy \
        scipy \
        matplotlib \
        pysam==0.15.4 \
    && apt-get purge -y --auto-remove python2-dev wget ca-certificates gcc \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN python2 -c "import misopy; print(misopy.__version__)"

WORKDIR /data
CMD ["miso"]
