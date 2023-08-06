FROM mambaorg/micromamba:1.4

ENV PATH=/opt/bin/:/opt/hamr/:$PATH
ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN micromamba install -y -c conda-forge -c bioconda -c anaconda -n base git r-base python=2.7 samtools bedtools make && \
    micromamba clean --all --yes && \
    micromamba shell init --shell bash --root-prefix=~/micromamba  \

ADD hamr /opt/
RUN cd /opt/hamr && \
    make clean && make

RUN chmod +x /opt/hamr/* &&  rm -rf /tmp/*
