ARG VERSION=2.4

FROM python:3.8.20-slim-bullseye
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN pip3 install --no-cache-dir \
    SUPPA==${VERSION} 

RUN suppa.py --help 2>&1

WORKDIR /data
CMD ["suppa.py"]
