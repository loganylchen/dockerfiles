FROM ubuntu:22.04


ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:/opt/eligos2/:/opt/eligos2/Scripts:$PATH
ARG SAMTOOLSVER=1.18


ADD https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static /opt/bin/bedtools

RUN apt-get update && apt-get install --no-install-recommends -y \
         libncurses5-dev \
         libbz2-dev \
         liblzma-dev \
         libcurl4-gnutls-dev \
         zlib1g-dev \
         libssl-dev \
         python3 \
         python3-pip \
         python3-dev \
         python3-setuptools \
         python3-rpy2 \
         gcc \
         wget \
         make \
         perl \
         bzip2 \
         g++ \
         gnuplot \
         ca-certificates \
         r-base \
         git \
         gawk && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 20 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN cd /tmp/ && \
    wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
    rm samtools-${SAMTOOLSVER}.tar.bz2 && \
    cd samtools-${SAMTOOLSVER} && \
    ./configure && \
    make && \
    make install  && \
    cd /opt/ &&  \
    pip install pysam pandas pybedtools rpy2  tqdm numpy && \
    Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")' && \
    cd /opt/ && \
    git clone https://gitlab.com/piroonj/eligos2.git && \
    chmod +x /opt/eligos2/* && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

