ARG VERSION=2.3

FROM ubuntu:20.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH="/opt/suppa:${PATH}"
RUN apt-get update && apt-get install -y wget unzip python3 python3-pip python3-dev && \
    pip3 install --no-cache-dir \
    SUPPA==${VERSION} && \
    wget https://github.com/comprna/SUPPA/archive/refs/tags/v${VERSION}.zip  && \
    unzip v${VERSION}.zip && \
    mv SUPPA-${VERSION} /opt/suppa && \
    chmod -R +x /opt/suppa && \
    ln -s /opt/suppa/suppa.py /usr/local/bin/suppa.py && \
    rm -rf /var/lib/apt/lists/* /root/.cache

RUN python3 /opt/suppa/suppa.py --help 2>&1

WORKDIR /data
CMD ["python3", "/opt/suppa/suppa.py"]
