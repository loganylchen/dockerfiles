ARG VERSION=2.1.0

# Based on official ELIGOS2 installation guide: https://gitlab.com/piroonj/eligos2
# Uses mambaorg/micromamba for faster dependency resolution

FROM mambaorg/micromamba:1.5.10
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ARG VERSION

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        procps \
    && rm -rf /var/lib/apt/lists/*

# Create the conda environment with mamba (following official guide)
RUN micromamba install -y -n base -c conda-forge -c bioconda -c r \
        pysam pandas pybedtools=0.8.0 bedtools=2.25 rpy2=2.8.5 r-base=3.4.1 tqdm numpy \
    && micromamba clean --all --yes

# Clone ELIGOS2
WORKDIR /opt
RUN git clone --depth=1 --branch v${VERSION} https://gitlab.com/piroonj/eligos2.git /opt/eligos2 && \
    rm -rf /opt/eligos2/.git

# Install R package (use micromamba run to execute in conda environment)
RUN micromamba run -n base Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")'

# Make ELIGOS2 scripts executable and add to PATH
RUN chmod +x /opt/eligos2/eligos2 /opt/eligos2/Scripts/*.py 2>/dev/null || true
ENV PATH="/opt/eligos2:/opt/eligos2/Scripts:${PATH}"

# Verify installation
RUN micromamba run -n base /opt/eligos2/eligos2 -h

WORKDIR /data

CMD ["micromamba", "run", "-n", "base", "/opt/eligos2/eligos2", "-h"]
