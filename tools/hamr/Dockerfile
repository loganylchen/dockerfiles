FROM python:3.11

ENV PATH=/opt/bin:/opt/hamr/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt update && \
    apt install -y bzip2 git r-base git make && \
    pip3 install rich

ADD https://github.com/samtools/samtools/releases/download/1.18/samtools-1.18.tar.bz2 /tmp
ADD https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static /opt/bin/bedtools

RUN git clone https://github.com/GregoryLab/HAMR.git /opt/hamr
#RUN git clone https://github.com/haydenji0731/HAMR.git /opt/hamr

ADD hamr.py /opt/hamr/hamr.py

RUN cd /tmp && \
    tar -jxvf samtools-1.18.tar.bz2 && \
    cd samtools-1.18/ && \
    ./configure && make && make install && \
    R -e 'install.packages(c("RColorBrewer"))' && \
    chmod +x /opt/bin/* /opt/hamr/* && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*  /opt/hamr/.git



