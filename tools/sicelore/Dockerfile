FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
ENV PATH /opt/bin/:/opt/FLAMES/python:/opt/FLAMES/src/bin/:/opt/minimap2-2.24_x64-linux/:$PATH
ARG VERSION
ARG packages='python2 python2-dev g++ git wget build-essential zlib1g-dev libbz2-dev liblzma-dev libcurl4-openssl-dev cmake openjdk-8-jdk libncurses5-dev'
ARG python_packages='cython numpy pysam editdistance'


RUN apt update \
    && apt install -y ${packages} \
    && wget https://bootstrap.pypa.io/pip/2.7/get-pip.py -O get-pip.py \
    && python2 get-pip.py \
    && pip2 install ${python_packages} \
    && mkdir -p /opt/bin \
    && ln -s /usr/bin/python2 /usr/bin/python \
    && git clone https://github.com/LuyiTian/FLAMES.git /opt/FLAMES \
    && cd /opt/FLAMES/src \
    && g++ -std=c++11  -O2 -o bin/match_cell_barcode ssw/ssw_cpp.cpp ssw/ssw.c match_cell_barcode.cpp kseq.h edit_dist.cpp -lz \
    && git clone https://github.com/lbcb-sci/racon /tmp/racon && cd /tmp/racon && mkdir build && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. && make && make install \
    && git clone https://github.com/rvaser/spoa /tmp/spoa && cd /tmp/spoa && mkdir build && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. && make && make install \
    && wget http://opengene.org/fastp/fastp -O /opt/bin/fastp &&  chmod a+x /opt/bin/fastp \
    && cd /tmp/ && wget https://github.com/samtools/samtools/releases/download/1.15.1/samtools-1.15.1.tar.bz2 -O /tmp/samtools-1.15.1.tar.bz2 \
    && tar -jxvf /tmp/samtools-1.15.1.tar.bz2 \
    && cd /tmp/samtools-1.15.1 \
    && ./configure && make && make install \
    && wget https://github.com/lh3/minimap2/releases/download/v2.24/minimap2-2.24_x64-linux.tar.bz2 -O /tmp/minimap2-2.24_x64-linux.tar.bz2 \
    && cd /tmp/ && tar -jxvf /tmp/minimap2-2.24_x64-linux.tar.bz2 \
    && cp -r /tmp/minimap2-2.24_x64-linux/  /opt/minimap2-2.24_x64-linux/\
    && git clone https://github.com/ucagenomix/sicelore.git /opt/sicelore \
    && rm -rf /tmp/*

ADD SiCeLoRe.bash /opt/bin/SiCeLoRe
RUN chmod a+x /opt/bin/SiCeLoRe

