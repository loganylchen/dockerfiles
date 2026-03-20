ARG VERSION=1.0

FROM qmcgaw/latexdevcontainer:latest-full
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        ghostscript \
        libfontconfig1 \
        fontconfig \
        libfontconfig1-dev \
        libfontconfig \
        python3-pip \
    && pip3 install --no-cache-dir Pygments \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
CMD bash
