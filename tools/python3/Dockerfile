FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt update -y \
    &&  apt -y install  \
    python3-pip \
    python3-dev \
    git \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 10


ADD requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt \
    # Remove build dir
    && apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
