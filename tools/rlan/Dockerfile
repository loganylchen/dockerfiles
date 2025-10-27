FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH


RUN micromamba install -y \
    conda-forge::r-ggplot2 \
    conda-forge::r-biocmanager \
    conda-forge::r-dplyr \
    conda-forge::r-ggpubr \
    conda-forge::r-ggsci \
    conda-forge::r-tidyr \
    conda-forge::r-tibble \
    conda-forge::r-devtools \
    conda-forge::r-readr \
    conda-forge::r-tidyverse \
    conda-forge::r-ggrepel \
    bioconda::bioconductor-enhancedvolcano \
    bioconda::bioconductor-deseq2 \
    && micromamba clean --all --yes

ADD ./install_R_packages.R /tmp/

RUN micromamba run -n base Rscript /tmp/install_R_packages.R 


