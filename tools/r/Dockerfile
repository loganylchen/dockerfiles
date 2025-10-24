FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt update -y \
    &&  apt -y install  \
    r-base \
    libssl-dev \
    libfontconfig1-dev \
    libmariadb-dev \
    libxml2-dev \
    libudunits2-dev \
    libcurl4-openssl-dev \
    cmake 

ADD install_R_packages.R /tmp/

RUN Rscript /tmp/install_R_packages.R \
    # Remove build dir
    && apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
