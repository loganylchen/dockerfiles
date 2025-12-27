FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y conda-forge::r-pheatmap conda-forge::r-ggplot2 \
    conda-forge::r-reshape2 \
    conda-forge::r-rcolorbrewer \
    conda-forge::r-dplyr \
    conda-forge::r-devtools \
    conda-forge::r-tidyverse \
    && micromamba run -n base R -e "devtools::install_github('KaiAragaki/tidy_estimate@v${VERSION}')" \
    && micromamba clean --all --yes


