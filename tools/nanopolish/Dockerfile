FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt update -y && \
    apt -y install gzip libhdf5-dev zlib1g-dev git automake autoconf wget gcc g++ make lbzip2 bzip2 libbz2-dev && \
    cd /tmp/ && \
    git clone https://github.com/jts/nanopolish.git --recursive && \
    cd nanopolish && \
    git checkout v${VERSION} &&\
    git submodule update --init --recursive && \
    make && \
    mkdir -p /opt/bin/ && cp nanopolish /opt/bin/ && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
