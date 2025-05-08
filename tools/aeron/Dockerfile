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
    for py_file in  AeronScripts/*.py; do if [ -f "$v" ]; then sed -i "1i #!/usr/bin/env python2" "$py_file"; fi done && \
    cp AeronScripts/* /opt/bin/ && \
    chmod +x /opt/bin/* 



RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*




