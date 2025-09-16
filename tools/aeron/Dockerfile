FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ARG SAMTOOLS_VERSION=1.22.1
ENV PATH=/opt/bin/:$PATH


RUN apt update && apt install -y git python2 python2-dev build-essential git cmake pkg-config libncurses-dev libbz2-dev  \
    protobuf-compiler libprotoc-dev libjansson-dev automake libtool \
    autoconf automake make gcc perl zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev libncurses5-dev \
    jq bc curl unzip redland-utils librdf-dev bison flex wget && \
    update-alternatives --install /usr/bin/python python /usr/bin/python2 1 && \
    mkdir -p /opt/bin && \
    cd /tmp && \
    git clone https://github.com/loganylchen/Aeron.git && \
    cd Aeron && \
    git checkout ${VERSION} && \
    cp Binaries/* /opt/bin/ && \
    cp AeronScripts/* /opt/bin/ && \
    chmod +x /opt/bin/*  && \
    cd /tmp/ && \
    wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 -O samtools.tar.bz2 && \
    tar -xjvf samtools.tar.bz2 && \
    cd samtools-${SAMTOOLS_VERSION} && \
    make && make install



RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*






