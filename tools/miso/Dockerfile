ARG VERSION=0.5.4

# python2 is not available on debian:bookworm-slim; keep ubuntu:20.04
FROM ubuntu:20.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="MISO" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="MISO - Mixture of Isoforms probabilistic isoform quantification (Python 2.7)" \
      org.opencontainers.image.source="https://miso.readthedocs.io" \
      org.opencontainers.image.licenses="GPL-2.0"

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
        'numpy==1.16.6' \
        'scipy==1.2.3' \
        'matplotlib==2.2.5' \
        'pysam==0.15.4' \
    && apt-get purge -y --auto-remove python2-dev gcc \
    && apt-get install -y --no-install-recommends libcurl4 \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN python2 -c "import misopy; print(misopy.__version__)"

WORKDIR /data
CMD ["miso"]
