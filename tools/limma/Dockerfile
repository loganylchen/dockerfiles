FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y -c conda-forge -c bioconda bioconductor-limma=${VERSION} r-dplyr bioconductor-edger \
    && micromamba clean --all --yes


