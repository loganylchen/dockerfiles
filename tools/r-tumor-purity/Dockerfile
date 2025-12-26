FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH


RUN micromamba install -y bioconda::r-immunedeconv==2.0.3 conda-forge::r-pheatmap conda-forge::r-ggplot2 \
    conda-forge::r-reshape2 \
    bioconda::bioconductor-gsva \
    bioconda::bioconductor-singscore \
    bu_cnio::r-estimate \
    conda-forge::r-rcolorbrewer \
    conda-forge::r-gridextra \
    conda-forge::r-corrplot \
    bioconda::bioconductor-complexheatmap \
    conda-forge::r-circlize \
    conda-forge::r-ggpubr \
    conda-forge::r-tidyverse \
    conda-forge::r-scales \
    conda-forge::r-viridis \
    && micromamba clean --all --yes 



