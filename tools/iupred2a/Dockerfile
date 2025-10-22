FROM ubuntu:22.04

ENV PATH=/opt/bin/:/opt/iupred2a/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION


ADD ./iupred2a.tar.gz /tmp/

RUN apt update -y \
    &&  apt -y install  \
    git wget make g++ \
    && cd /tmp \
    && mv iupred2a /opt/iupred2a \ 
    && chmod -R +x /opt/ \
    && apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
