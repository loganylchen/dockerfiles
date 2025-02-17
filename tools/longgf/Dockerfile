FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV VERSION=0.1.2
ENV PATH=/opt/bin/:$PATH
ENV C_INCLUDE_PATH=/opt/softwares/htslib/include
ENV CPLUS_INCLUDE_PATH=/opt/softwares/htslib/include
ENV LD_LIBRARY_PATH=/opt/softwares/htslib/lib/

RUN apt update && apt install -y wget build-essential g++ zlib1g-dev libbz2-dev \
    liblzma-dev && \
    cd /tmp && \
    wget https://github.com/samtools/htslib/releases/download/1.12/htslib-1.12.tar.bz2 && \
    tar -jxvf htslib-1.12.tar.bz2 && \
    cd htslib-1.12 && \
    ./configure --prefix=/opt/softwares/htslib && make && make install && \
    cd /tmp && \
    wget https://github.com/WGLab/LongGF/archive/refs/tags/v${VERSION}.tar.gz && \
    tar -vxzf v${VERSION}.tar.gz && \
    cd LongGF-${VERSION}/bin && \
    g++ -g -Wall -O3 -std=c++11 -I/opt/softwares/htslib/include -L/opt/softwares/htslib/lib -lhts -o LongGF _com_fun_.c _gtf_struct_.c get_gfFrombam.c /opt/softwares/htslib/lib/libhts.so && \
    mkdir -p /opt/bin/ && \
    cp LongGF /opt/bin/


RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*



