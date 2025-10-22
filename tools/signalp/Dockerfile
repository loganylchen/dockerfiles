FROM ubuntu:22.04

ENV PATH=/opt/bin/:/opt/singalp/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION


ADD ./signalp-5.0b.Linux.tar.gz /tmp/

RUN apt update -y \
    &&  apt -y install  \
    git wget make g++ \
    && cd /tmp \
    && mv signalp-5.0b /opt/signalp \ 
    && chmod -R +x /opt/ \
    && apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
