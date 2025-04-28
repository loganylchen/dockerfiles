FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:/opt/conda/RNA-m5C:$PATH
ARG VERSION
ARG HISAT2_VERSION=2.1.0
ARG BOWTIE_VERSION=2.3.5
ARG SAMTOOLS_VERSION=1.6

RUN micromamba install -y -c conda-forge -c bioconda -c anaconda \
    git \
    python=2.7 \
    hisat2=${HISAT2_VERSION} \
    bowtie2=${BOWTIE_VERSION} \
    samtools=${SAMTOOLS_VERSION} &&\
    pip install numpy==1.13.3 \
    scipy==0.19.1 \
    pysam==0.12.0.1 \
    biopython==1.70 &&\
    git clone https://github.com/loganylchen/RNA-m5C.git /opt/conda/RNA-m5C &&\
    cd /opt/conda/RNA-m5C &&\
    git checkout ${VERSION} &&\
    micromamba clean --all --yes


