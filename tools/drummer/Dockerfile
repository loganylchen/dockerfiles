FROM ubuntu:322.04


ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH
ARG SAMTOOLSVER=1.18

ADD DRUMMER /opt/bin/

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    wget \
    unzip \
    bzip2 \
    git \
    libidn11* \
    python3-pip \
    samtools \
    bedtools

RUN cd /opt/ &&  \
    git clone https://github.com/DepledgeLab/DRUMMER && \
    pip install seaborn scipy pandas numpy biopython matplotlib statsmodels && \
    chmod -R +x /opt/bin/ && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/* /var/lib/apt/lists/*

