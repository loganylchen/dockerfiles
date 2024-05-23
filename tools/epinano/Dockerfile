FROM ubuntu:18.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y  \
    python3 python3-pip python3-dev python3-h5py python3-numpy software-properties-common dirmngr \
    build-essential make libssl-dev zlib1g-dev libharfbuzz-dev libfribidi-dev \
    libbz2-dev libreadline-dev libsqlite3-dev   llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev libxml2-dev \
    libgdbm-dev libnss3-dev libedit-dev libc6-dev libhdf5-dev curl libcurl4-openssl-dev \
    zlib1g-dev git automake libhdf5-serial-dev \
    autoconf wget gcc g++  lbzip2 bzip2 cmake openjdk-8-jdk ant && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 20 &&\
    python -m pip install --upgrade pip && \
    wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc |  tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc && \
    add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran35/" && \
    apt-get update && \
    apt-get install -y r-base r-base-dev && \
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
RUN cd /tmp/ && pip3.6 install -r /tmp/requirements.txt && \
    Rscript /tmp/install_packages_R.R && \
    wget https://github.com/novoalab/EpiNano/archive/refs/tags/EpiNano1.2.3.tar.gz && \
    tar -zxvf EpiNano1.2.3.tar.gz && \
    mv EpiNano-EpiNano1.2.3 /opt/EpiNano && \
    wget https://github.com/novoalab/EpiNano/raw/master/misc/sam2tsv.jar -P /opt/EpiNano/ && \
    cd /opt/EpiNano/ && \
    chmod -R +x /opt/bin/ && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*


