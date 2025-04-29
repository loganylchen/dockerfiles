FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH=/opt/bin/:$PATH


RUN apt update && apt install -y git python2 python2-dev build-essential git cmake pkg-config libncurses-dev libbz2-dev  \
    protobuf-compiler libprotoc-dev libjansson-dev automake libtool \
    jq bc curl unzip redland-utils librdf-dev bison flex && \
    mkdir -p /opt/bin && \
    cd /tmp && \
    git clone https://github.com/SchulzLab/Aeron.git && \
    cd Aeron && \
    git checkout ${VERSION} && \
    cp Binaries/* /opt/bin/ && \
    cp AeronScripts/* /opt/bin/ && \
    cd /tmp && \
    git clone --recursive https://github.com/vgteam/vg.git && \
    cd vg && \
    git checkout v1.5.0 && \
    git submodule update --init --recursive && \
    . /tmp/vg/source_me.sh && make &&\
    cp bin/* /opt/bin/ &&\
    chmod +x /opt/bin/* 



RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*




