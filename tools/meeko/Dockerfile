FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH
ENV PYTHONPATH=/usr/local/lib:$PYTHONPATH

RUN apt update && apt install -y wget build-essential gzip && \
    cd /tmp && \
    wget https://udomain.dl.sourceforge.net/project/openbabel/openbabel/2.3.1/openbabel-2.3.1.tar.gz && \
    tar -zxvf openbabel-2.3.1.tar.gz && \
    mkdir build && \
    cd build && \
    cmake ../openbabel-2.3.1 -DPYTHON_BINDINGS=ON && \
    make -j4 && \
    make install && \
    pip install numpy   && \
    pip install meeko && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*
