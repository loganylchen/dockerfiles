FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive



RUN apt update -y && \
    apt install -y \
    python3 python3-dev python3-pip \
    r-base libcurl4-openssl-dev libssl-dev \
    libxml2-dev libproj-dev libfontconfig1-dev git liblz4-dev libzstd-dev \
    libharfbuzz-dev libfribidi-dev build-essential && \
    rm -rf /tmp/*

