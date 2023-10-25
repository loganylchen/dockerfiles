FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ENV PLUGIN_PATH=$HOME/.local/hdf5/lib/plugin

RUN apt update -y && \
    apt -y install libhdf5-dev zlib1g-dev git wget tar gcc g++ make autoconf bash && \
    cd /tmp/ && \
    git clone --recursive https://github.com/hasindu2008/slow5tools && \
    cd slow5tools && \
    bash scripts/install-vbz.sh && \
    git checkout bad_fast5 && \
    autoreconf --install && ./configure && make && \
    mkdir -p /opt/bin/ && cp slow5tools /opt/bin/ && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
