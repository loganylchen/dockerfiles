ARG VERSION=2.3

FROM python:3.4.10-alpine3.8
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH="/opt/suppa:${PATH}"
RUN apt-get update && apt-get install -y wget unzip && \
    pip3 install --no-cache-dir \
    SUPPA==${VERSION} && \
    wget https://github.com/comprna/SUPPA/archive/refs/tags/v${VERSION}.zip  && \
    unzip v${VERSION}.zip && \
    mv SUPPA-${VERSION} /opt/suppa && \
    chmod -R +x /opt/suppa && \
    ln -s /opt/suppa/suppa.py /usr/local/bin/suppa.py && \
    rm -rf /var/lib/apt/lists/* /root/.cache

RUN suppa.py --help 2>&1

WORKDIR /data
CMD ["suppa.py"]
