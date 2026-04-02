ARG VERSION=1.1.2

FROM ubuntu:20.04
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
        git \
        bedtools \
    && wget -q https://bootstrap.pypa.io/pip/2.7/get-pip.py -O /tmp/get-pip.py \
    && python2 /tmp/get-pip.py \
    && pip2 install --no-cache-dir \
        'numpy==1.16.6' \
        'pandas==0.24.2' \
        'pysam==0.15.4' \
    && pip2 install --no-cache-dir \
        git+https://github.com/yarden/rnaseqlib.git \
    && wget -q https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/gtfToGenePred \
        -O /usr/local/bin/gtfToGenePred \
    && chmod +x /usr/local/bin/gtfToGenePred \
    && apt-get purge -y --auto-remove python2-dev wget ca-certificates gcc git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN python2 -c "import rnaseqlib; print('rnaseqlib OK')" \
    && gtfToGenePred 2>&1 || true

WORKDIR /data
CMD ["gff_make_annotation"]
