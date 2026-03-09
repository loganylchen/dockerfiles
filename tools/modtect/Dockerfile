FROM ubuntu:18.04

ENV PATH=/opt/bin:/opt/modtect/:$PATH
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends samtools git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ktan8/ModTect.git /opt/modtect/
ADD modtect.py /opt/modtect/modtect.py
RUN chmod +x /opt/modtect/* && \
    rm -rf /tmp/*
