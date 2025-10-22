FROM ubuntu:22.04

ENV PATH=/opt/bin/:/opt/PUREE/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt update -y \
    &&  apt -y install  \
    python3-pip \
    python3-dev \
    git \
    && cd /opt/ \
    && git clone https://github.com/skandlab/PUREE.git \
    && cd PUREE \
    && git checkout ${VERSION} \
    && pip install -r requirements.txt 

ADD PUREE /opt/PUREE/

RUN chmod -R +x /opt  \
    # Remove build dir
    && apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
