FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y bioconda::r-immunedeconv=${VERSION} conda-forge::r-pheatmap conda-forge::r-ggplot2 \
    conda-forge::r-reshape2 \
    bioconda::bioconductor-gsva \
    bioconda::bioconductor-singscore \
    && micromamba clean --all --yes


