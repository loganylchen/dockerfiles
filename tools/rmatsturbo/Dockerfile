FROM ubuntu:22.04

ENV PATH=/opt/bin/:/opt/rmats/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION=4.3.0

RUN apt update -y && \
    apt -y install  gcc build-essential   python3-pip \
    ca-certificates \
    cmake \
    curl \
    cython3 \
    g++ \
    gfortran \
    git \
    libblas-dev \
    libgsl-dev \
    liblapack-dev \
    make \
    python-is-python3 \
    python3-dev \
    r-base \
    r-cran-doparallel \
    r-cran-dosnow \
    r-cran-foreach \
    r-cran-getopt \
    r-cran-ggplot2 \
    r-cran-iterators \
    r-cran-mixtools \
    r-cran-nloptr \
    r-cran-rcpp \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* 

RUN cd /tmp/ && \
    mkdir rmats_build \
    && cd rmats_build \
    && git clone https://github.com/Xinglab/rmats-turbo.git \
    && cd rmats-turbo \
    && git checkout v${VERSION} \
    # The build will source setup_environment.sh which will source ~/.bashrc.
    # Skip that by truncating setup_environment.sh
    && echo '' > setup_environment.sh \
    && ./build_rmats \
    # Copy the build results
    && mkdir -p rmats \
    && cd rmats \
    && cp /tmp/rmats_build/rmats-turbo/rmats.py ./ \
    && cp /tmp/rmats_build/rmats-turbo/cp_with_prefix.py ./ \
    && cp /tmp/rmats_build/rmats-turbo/*.so ./ \
    && mkdir rMATS_C \
    && cp /tmp/rmats_build/rmats-turbo/rMATS_C/rMATSexe ./rMATS_C \
    && mkdir rMATS_P \
    && cp /tmp/rmats_build/rmats-turbo/rMATS_P/*.py ./rMATS_P \
    && mkdir rMATS_R \
    && cp /tmp/rmats_build/rmats-turbo/rMATS_R/*.R ./rMATS_R \
    && cp -r ../rmats /opt && \
    && chmod -R +x /opt &&\
    # Remove build dir
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
