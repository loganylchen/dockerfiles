FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH=/opt/bin/:$PATH


RUN apt update && apt install -y lftp curl && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*
