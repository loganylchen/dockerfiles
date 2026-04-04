ARG VERSION=1.0

# sicelore: requires python2, openjdk, C++ compilation — keep ubuntu base
FROM ubuntu:20.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin/:/opt/FLAMES/python:/opt/FLAMES/src/bin/:/opt/minimap2-2.24_x64-linux/:$PATH
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python2 python2-dev \
        g++ git wget \
        build-essential \
        zlib1g-dev libbz2-dev liblzma-dev \
        libcurl4-openssl-dev \
        cmake \
        openjdk-8-jdk \
        libncurses5-dev \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q https://bootstrap.pypa.io/pip/2.7/get-pip.py -O /tmp/get-pip.py \
    && python2 /tmp/get-pip.py \
    && pip2 install --no-cache-dir cython numpy pysam editdistance \
    && rm /tmp/get-pip.py

RUN mkdir -p /opt/bin \
    && ln -s /usr/bin/python2 /usr/bin/python \
    && git clone --depth=1 https://github.com/LuyiTian/FLAMES.git /opt/FLAMES \
    && cd /opt/FLAMES/src \
    && g++ -std=c++11 -O2 -o bin/match_cell_barcode \
        ssw/ssw_cpp.cpp ssw/ssw.c match_cell_barcode.cpp kseq.h edit_dist.cpp -lz

RUN git clone --depth=1 https://github.com/lbcb-sci/racon /tmp/racon \
    && cd /tmp/racon && mkdir build && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. && make -j$(nproc) && make install \
    && git clone --depth=1 https://github.com/rvaser/spoa /tmp/spoa \
    && cd /tmp/spoa && mkdir build && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. && make -j$(nproc) && make install

RUN wget -q https://opengene.org/fastp/fastp -O /opt/bin/fastp \
    && chmod +x /opt/bin/fastp \
    && wget -q https://github.com/samtools/samtools/releases/download/1.15.1/samtools-1.15.1.tar.bz2 -O /tmp/samtools.tar.bz2 \
    && tar -jxf /tmp/samtools.tar.bz2 -C /tmp \
    && cd /tmp/samtools-1.15.1 \
    && ./configure && make -j$(nproc) && make install \
    && wget -q https://github.com/lh3/minimap2/releases/download/v2.24/minimap2-2.24_x64-linux.tar.bz2 -O /tmp/minimap2.tar.bz2 \
    && tar -jxf /tmp/minimap2.tar.bz2 -C /tmp \
    && cp -r /tmp/minimap2-2.24_x64-linux/ /opt/minimap2-2.24_x64-linux/ \
    && git clone https://github.com/ucagenomix/sicelore.git /opt/sicelore \
    && rm -rf /tmp/*

ADD SiCeLoRe.bash /opt/bin/SiCeLoRe
RUN chmod +x /opt/bin/SiCeLoRe

RUN samtools --version

WORKDIR /data
CMD ["bash"]
