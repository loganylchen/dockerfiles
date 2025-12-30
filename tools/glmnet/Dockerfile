FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y conda-forge::r-glmnet=${VERSION} \
    conda-forge::r-pheatmap \
    conda-forge::r-ggplot2 \
    conda-forge::r-reshape2 \
    conda-forge::r-proc \
    conda-forge::r-dplyr \
    conda-forge::r-readr \
    conda-forge::r-tidyr \
    conda-forge::r-caret \
    conda-forge::r-ggsci \
    && micromamba clean --all --yes

