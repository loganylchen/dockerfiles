ARG VERSION=2.5

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
        git \
        ca-certificates \
        libhts-dev \
        libhdf5-dev \
        pkg-config \
        zlib1g-dev \
    && git clone --depth 1 --branch v${VERSION} \
        https://bitbucket.org/biociphers/majiq_academic.git /tmp/majiq \
    && pip3 install --no-cache-dir --break-system-packages /tmp/majiq/voila \
    && pip3 install --no-cache-dir --break-system-packages /tmp/majiq/majiq \
    && pip3 install --no-cache-dir --break-system-packages 'click<8.0' \
    && apt-get purge -y --auto-remove python3-dev gcc g++ git ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/majiq /root/.cache

RUN python3 -c "import rna_majiq; print('majiq OK')"

WORKDIR /data
CMD ["majiq"]
