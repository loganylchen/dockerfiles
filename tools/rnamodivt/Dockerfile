FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:/opt/conda/RNAMod:$PATH
ARG VERSION
ARG HISAT2_VERSION=2.1.0
ARG SAMTOOLS_VERSION=1.6
ARG BEDTOOLS_VERSION=2.29.2
ARG MACS2_VERSION=2.1.2 
ARG EXOMEPEAK2_VERSION=1.3.7

RUN micromamba install -y -c conda-forge -c bioconda -c anaconda \
    git \
    python=2.7 \
    r-base=3.5.1 \
    perl \
    hisat2=${HISAT2_VERSION} \
    macs2=${MACS2_VERSION} \
    bioconductor-exomepeak2=${EXOMEPEAK2_VERSION} \
    bedtools=${BEDTOOLS_VERSION} \
    samtools=${SAMTOOLS_VERSION} &&\
    pip install numpy==1.13.3 \
    scipy==0.19.1 \
    pysam==0.12.0.1 \
    biopython==1.70 &&\
    git clone https://github.com/Epigenomics-Lab/RNAMod.git /opt/conda/RNAMod &&\
    cd /opt/conda/RNAMod &&\
    git checkout ${VERSION} &&\
    micromamba clean --all --yes


