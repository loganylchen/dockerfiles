FROM python:2.7

ENV PATH=/opt/bin:/opt/modtect/:$PATH

RUN apt update && \
    apt install -y bzip2 git

ADD https://github.com/samtools/samtools/releases/download/1.18/samtools-1.18.tar.bz2 /tmp

RUN cd /tmp/ && \
    tar -jxvf samtools-1.18.tar.bz2 && \
    mkdir /opt/bin && \
    cd samtools-1.18/ && \
    ./configure && make && make install && \
    git clone https://github.com/ktan8/ModTect.git /opt/modtect/
ADD modtect.py /opt/modtect/modtect.py
RUN chmod +x  /opt/modtect/* && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

