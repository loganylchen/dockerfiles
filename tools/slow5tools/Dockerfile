FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ENV PLUGIN_PATH=/usr/local/lib/
ENV HDF5_PLUGIN_PATH=${PLUGIN_PATH}
ENV ARCH=x86_64
ENV OS=GNU/Linux
ENV ONT_VBZ_VERSION=v1.0.1
ENV ONT_VBZ_FILE=ont-vbz-hdf-plugin-1.0.1-Linux-${ARCH}.tar.gz
ENV ONT_VBZ_DIR=/tmp/ont_vbz_plugin_$ONT_VBZ_VERSION
ARG VERSION

RUN apt update -y && \
    apt -y install libhdf5-dev zlib1g-dev git wget tar gcc g++ make autoconf bash && \
    wget https://github.com/nanoporetech/vbz_compression/releases/download/$ONT_VBZ_VERSION/$ONT_VBZ_FILE -O /tmp/$ONT_VBZ_FILE && \
    mkdir -p $ONT_VBZ_DIR && \
    tar -xzvf  /tmp/$ONT_VBZ_FILE -C $ONT_VBZ_DIR && \
    find $ONT_VBZ_DIR -name '*.so' -exec mv -t $PLUGIN_PATH {} + && \
    cd /tmp/ && \
    git clone --recursive https://github.com/hasindu2008/slow5tools && \
    cd slow5tools && \
    git checkout v${VERSION} &&\
    git submodule update --init --recursive && \
    autoreconf --install && ./configure && make && \
    mkdir -p /opt/bin/ && cp slow5tools /opt/bin/ && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*




