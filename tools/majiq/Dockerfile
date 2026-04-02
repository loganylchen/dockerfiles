ARG VERSION=2.5

FROM ubuntu:20.04
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
        zlib1g-dev \
    && git clone --depth 1 --branch v${VERSION} \
        https://bitbucket.org/biociphers/majiq_academic.git /tmp/majiq \
    && pip3 install --no-cache-dir /tmp/majiq/voila \
    && pip3 install --no-cache-dir /tmp/majiq/majiq \
    && pip3 install --no-cache-dir 'click<8.0' \
    && apt-get purge -y --auto-remove python3-dev gcc g++ git ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/majiq /root/.cache

RUN python3 -c "import sys; print(sys.path)" \
    && pip3 show rna-majiq 2>/dev/null || true \
    && find /usr -path '*/majiq*' -type f 2>/dev/null | head -20 || true \
    && python3 -c "import majiq; print('majiq OK')"

WORKDIR /data
CMD ["majiq"]
