FROM mambaorg/micromamba:1.4

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive


RUN micromamba install -y -c conda-forge -c bioconda -c anaconda -n base git r-base python=2.7 samtools bedtools && \
    micromamba clean --all --yes && \
    git clone https://github.com/GregoryLab/HAMR.git /opt/hamr && \
    cd /opt/hamr && \
    make clean && make
COPY hamr.py /opt/hamr/hamr.py
RUN chmod +x /opt/hamr/* &&  rm -rf /tmp/*
