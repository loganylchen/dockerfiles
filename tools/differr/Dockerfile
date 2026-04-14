ARG VERSION=0.2

FROM python:3.7.17-alpine3.18
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apk add --no-cache --virtual .build-deps \
    git \
    g++ \
    gcc \
    && pip install --no-cache-dir git+https://github.com/bartongroup/differr_nanopore_DRS.git@${VERSION} \
    && apk del .build-deps \
    && rm -rf /tmp/* /root/.cache 

# Smoke-test
RUN differr --help

WORKDIR /data

CMD ["differr", "--help"]
