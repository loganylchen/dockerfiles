FROM ubuntu:18.04

ENV PATH=/opt/bin:/opt/modtect/:$PATH

RUN apt update && \
    apt install -y samtools git

RUN git clone https://github.com/ktan8/ModTect.git /opt/modtect/
ADD modtect.py /opt/modtect/modtect.py
RUN chmod +x  /opt/modtect/* && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

