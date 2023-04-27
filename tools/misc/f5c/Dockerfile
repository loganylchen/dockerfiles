FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive


RUN apt update -y && \
    apt -y install libhdf5-dev zlib1g-dev git automake autoconf wget gcc g++ make && \
    cd /tmp/ && \
    git clone --recursive https://github.com/hasindu2008/f5c && \
    cd f5c && \
    git checkout edparam && \
    autoreconf --install && scripts/install-hts.sh && ./configure --disable-hdf5 && make && \
    mkdir -p /opt/bin/ && cp f5c /opt/bin/ && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*