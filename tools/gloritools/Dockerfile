FROM ubuntu:22.04

ENV PATH=/opt/GLORI-tools:/opt/bin:$PATH
ENV STAR_VERSION=2.7.11b
ENV BOWTIE_VERSION=1.3.1
ENV SAMTOOLS_VERSION=1.19

RUN apt-get update && \
    apt-get install -y git curl wget python3 python3-dev python3-pip build-essential xxd zip libncurses5-dev libbz2-dev liblzma-dev && \
    cd /tmp && \
    mkdir -p /opt/bin/ && \
    wget https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz && \
    tar -xzf ${STAR_VERSION}.tar.gz && \
    cp STAR-${STAR_VERSION}/bin/Linux_x86_64/STAR* /usr/local/bin/ && \
    cd /tmp && \
    wget https://altushost-swe.dl.sourceforge.net/project/bowtie-bio/bowtie/${BOWTIE_VERSION}/bowtie-${BOWTIE_VERSION}-src.zip && \
    unzip bowtie-${BOWTIE_VERSION}-src.zip && \ 
    cd bowtie-${BOWTIE_VERSION}-src && \
    make && make install && \
    cd /tmp/ && \
    wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
    tar -jxvf samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VERSION} && \
    ./configure && make && make install && \
    ln -s /usr/bin/python3 /usr/bin/python 

ADD requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt && \
    cd /opt/ && \
    git clone https://github.com/liucongcas/GLORI-tools.git && \
    rm -rf /tmp/* 

WORKDIR /opt/




