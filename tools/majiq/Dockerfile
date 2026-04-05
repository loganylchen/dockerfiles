ARG VERSION=2.5

# python:3.9-slim — majiq v2.5 is incompatible with Python 3.11 on bookworm
FROM python:3.9-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
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
    && pip install --no-cache-dir 'numpy<1.24' \
    && pip install --no-cache-dir /tmp/majiq/voila \
    && pip install --no-cache-dir /tmp/majiq/majiq \
    && pip install --no-cache-dir 'click<8.0' \
    && pip install --no-cache-dir --force-reinstall --no-deps 'h5py<3.8' \
    && apt-get install -y --no-install-recommends libgomp1 \
    && apt-get purge -y python3-dev gcc g++ git ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/majiq /root/.cache

RUN python -c "import rna_majiq; print('majiq OK')"

WORKDIR /data
CMD ["majiq"]
