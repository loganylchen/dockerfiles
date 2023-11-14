FROM python:3.11.4
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH


RUN apt update && \
    apt install git && \
    pip install git+https://github.com/a-slide/NanoCount.git && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

