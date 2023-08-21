FROM ubuntu:22.04


ENV PATH=/opt/bin/:/opt/mgltools/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive


RUN apt update && apt install -y wget build-essential gzip && \
    cd /tmp && \
    wget https://ccsb.scripps.edu/download/532/ -O test2.tar.gz && \
    tar -zxvf test2.tar.gz && \
    cd mgltools_x86_64Linux2_1.5.7/ && \
    ./install.sh -d /opt/mgltools

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*



