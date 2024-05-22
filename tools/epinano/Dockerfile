FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y  \
    build-essential make libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev   llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
libgdbm-dev libnss3-dev libedit-dev libc6-dev libhdf5-dev curl zlib1g-dev git automake  \
    autoconf wget gcc g++  lbzip2 bzip2 r-base cmake openjdk-8-jdk ant

RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tgz && \
    tar -xzf Python-3.6.7.tgz && \
    cd Python-3.6.7 && \
    ./configure --enable-optimizations  -with-lto  --with-pydebug && \
    make -j 8  && make altinstall && \
    update-alternatives --install /usr/bin/python python /usr/local/bin/python3.6 20 &&\
    cd /tmp/ &&\
    mkdir -p /opt/bin/ && \
    curl -L https://github.com/lh3/minimap2/releases/download/v2.28/minimap2-2.28_x64-linux.tar.bz2 | tar -jxvf - && \
    mv ./minimap2-2.28_x64-linux/minimap2 /opt/bin/ && \
    wget https://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2/download -O samtools-0.1.19.tar.bz2  && \
    tar -jxvf samtools-0.1.19.tar.bz2 && \
    cd samtools-0.1.19 && \
    make && \
    cp samtools /opt/bin/


ADD requirements.txt /tmp/
ADD install_packages_R.R /tmp/
ADD epinano_variants /opt/bin/
RUN cd /tmp/ && pip3 install -r /tmp/requirements.txt && \
    Rscript /tmp/install_packages_R.R && \
    wget https://github.com/novoalab/EpiNano/archive/refs/tags/EpiNano1.2.3.tar.gz && \
    tar -zxvf EpiNano1.2.3.tar.gz && \
    mv EpiNano-EpiNano1.2.3 /opt/EpiNano && \
    wget https://github.com/novoalab/EpiNano/raw/master/misc/sam2tsv.jar -P /opt/EpiNano/ && \
    cd /opt/EpiNano/ && \
    chmod -R +x /opt/bin/ && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*


