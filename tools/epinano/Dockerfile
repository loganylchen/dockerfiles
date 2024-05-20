FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive


RUN apt update -y && \
    apt -y install libhdf5-dev curl zlib1g-dev git automake autoconf wget gcc g++ make lbzip2 bzip2 python3 python3-pip python3-dev r-base  && \
    cd /tmp/ &&\
    mkdir -p /opt/bin/ && \
    curl -L https://github.com/lh3/minimap2/releases/download/v2.28/minimap2-2.28_x64-linux.tar.bz2 | tar -jxvf - && \
    mv ./minimap2-2.28_x64-linux/minimap2 /opt/bin/ && \
    wget https://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2/download -O samtools-0.1.19.tar.bz2  && \
    tar -jxvf samtools-0.1.19.tar.bz2 && \
    cd samtools-0.1.19 && \
    make && \
    cp samtools /opt/bin/ && \
    cd /tmp/ && pip install cython


ADD requirements.txt /tmp/
ADD install_packages_R.R /tmp/
ADD epinano_variants /opt/bin/
RUN pip install -r /tmp/requirements.txt && \
    Rscript /tmp/install_packages_R.R && \
    git clone https://github.com/novoalab/EpiNano.git /opt/EpiNano/ && \
    cd /opt/EpiNano/ && \
    git checkout Epinano1.2.3 && \
    wget https://github.com/novoalab/EpiNano/raw/master/misc/sam2tsv.jar /opt/EpiNano/ && \
    chmod -R +x /opt/bin/ && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*


