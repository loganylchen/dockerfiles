FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV VERSION=1.1.1
ENV PATH=/opt/bin/:$PATH


RUN apt update && apt install -y wget make zlib1g-dev g++ gcc && \
    cd /tmp && \
    wget https://github.com/vpc-ccg/genion/archive/refs/tags/${VERSION}.tar.gz && \
    tar -vxzf ${VERSION}.tar.gz && \
    cd genion-${VERSION} && \
    make && \
    mkdir -p /opt/bin/ && \
    cp genion /opt/bin/


RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*




