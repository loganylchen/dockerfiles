FROM python:3.11.4


ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH
ARG SAMTOOLSVER=1.18


ADD https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static /opt/bin/bedtools
ADD DRUMMER /opt/bin/

RUN apt-get update && apt-get install --no-install-recommends -y \
         libncurses5-dev \
         libbz2-dev \
         liblzma-dev \
         libcurl4-gnutls-dev \
         zlib1g-dev \
         libssl-dev \
         gcc \
         wget \
         make \
         perl \
         bzip2 \
         gnuplot \
         ca-certificates \
         gawk && \
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
    git clone https://github.com/DepledgeLab/DRUMMER && \
    pip install seaborn scipy pandas numpy biopython matplotlib && \
    chmod -R +x /opt/bin/ && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

