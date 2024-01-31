FROM ubuntu:22.04

ENV PATH=/opt/bin/:/opt/psinanopore/:$PATH
ENV DEBIAN_FRONTEND=noninteractive


RUN apt update -y && \
    apt -y install libhdf5-dev zlib1g-dev git automake autoconf wget gcc g++ make lbzip2 bzip2 r-base && \
    cd /tmp/ && \
    Rscript -e 'install.packages(c("BiocManager","ggplot2","optparse"), repos="http://cran.us.r-project.org")' && \
    Rscript -e 'BiocManager::install("Biobase")' && \
    Rscript -e 'BiocManager::install("Rsamtools")' && \
    Rscript -e 'BiocManager::install("BSgenome")' && \
    git clone https://github.com/RouhanifardLab/PsiNanopore.git /opt/psinanopore && \
    sed -i 's/wdir = getwd( )/wdir = "\/opt\/psinanopore\/" /' /opt/psinanopore/PsiDetect.R && \
    sed -i 's/wdir = getwd( )/wdir = "\/opt\/psinanopore\/" /' /opt/psinanopore/SignalView.R && \
    chmod +x /opt/psinanopore/* && \
    apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
