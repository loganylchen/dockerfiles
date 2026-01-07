FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y -c conda-forge -c bioconda sra-tools=${VERSION} \
    pigz=2.8 conda-forge::lftp \
    && micromamba clean --all --yes


