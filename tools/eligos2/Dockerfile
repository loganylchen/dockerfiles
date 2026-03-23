ARG VERSION=2.1.0

# Based on official ELIGOS2 Dockerfile: https://gitlab.com/piroonj/eligos2
# Uses conda/miniconda3 base for compatibility with pinned versions

FROM conda/miniconda3
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION





WORKDIR /opt/eligos2

# Create the environment with pinned versions (as per official Dockerfile)
RUN conda install -y -c bioconda -c conda-forge -c anaconda \
    python=3.6 \
    pysam=0.13 \
    pandas=0.23.4 \
    pybedtools=0.8.0 \
    bedtools=2.25 \
    rpy2=2.8.5 \
    r-base=3.4.1 \
    tqdm=4.40.2 \
    numpy=1.11.3 \
    git

# Clone ELIGOS2
RUN git clone --depth=1 --branch v${VERSION} https://gitlab.com/piroonj/eligos2.git /opt/eligos2
# Install R package
RUN Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")'

# Add ELIGOS2 to PATH
ENV PATH="/opt/eligos2:/opt/eligos2/Scripts:$PATH"

# Verify installation
RUN eligos2 -h

WORKDIR /data

CMD ["eligos2", "-h"]
