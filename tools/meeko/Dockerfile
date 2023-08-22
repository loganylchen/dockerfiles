FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH
ENV PYTHONPATH=/usr/local/lib:$PYTHONPATH

RUN apt update && apt install -y wget build-essential gzip cmake libxml2-dev zlib1g-dev libeigen3-dev  python3-dev  python3-pip libcairo2-dev \
    python3-rdkit librdkit1 rdkit-data && \
    cd /tmp && \
    wget https://jaist.dl.sourceforge.net/project/openbabel/openbabel/2.4.0/openbabel-openbabel-2-4-0.tar.gz && \
    tar -zxvf openbabel-openbabel-2-4-0.tar.gz && \
    mkdir build && \
    cd build && \
    cmake ../openbabel-openbabel-2-4-0 -DPYTHON_BINDINGS=ON && \
    make -j4 && \
    make install && \
    pip install numpy scipy pandas   && \
    pip install meeko && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*
