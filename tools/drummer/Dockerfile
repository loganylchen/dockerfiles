FROM ubuntu:22.04


ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:/opt/DURMMER:$PATH
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
    bedtools && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 20

RUN cd /opt/ &&  \
    git clone https://github.com/loganylchen/DRUMMER && \
    pip install seaborn scipy pandas numpy biopython matplotlib statsmodels && \
    chmod -R +x /opt/bin/ && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/* /var/lib/apt/lists/*

