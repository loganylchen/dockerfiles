ARG VERSION=2.3

FROM python:3.4.10-alpine3.8
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN pip3 install --no-cache-dir \
    SUPPA==${VERSION} 

RUN suppa.py --help 2>&1

WORKDIR /data
CMD ["suppa.py"]
