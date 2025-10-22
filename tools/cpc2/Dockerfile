FROM ubuntu:22.04

ENV PATH=/opt/bin/:/opt/CPC2/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt update -y \
    &&  apt -y install  \
    python3-pip \
    python3-dev \
    python3 \
    git wget make g++ \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1 \
    && pip install biopython \
    && cd /tmp \
    && wget https://github.com/gao-lab/CPC2_standalone/archive/refs/tags/v${VERSION}.tar.gz \
    && tar -zxvf v${VERSION}.tar.gz \
    && cd CPC2_standalone-1.0.1/libs/libsvm \
    && tar -zxvf libsvm-3.18.tar.gz \
    && cd libsvm-3.18 \
    && make clean && make \
    && cd /opt/ \
    && mv /tmp/CPC2_standalone-1.0.1 /opt/CPC2 \
    && ln -s /opt/CPC2/bin/CPC2.py /usr/local/bin/CPC2 \
    && chmod -R +x /opt/ \
    && apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
