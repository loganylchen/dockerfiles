FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y -c conda-forge -c bioconda bioconductor-bambu=${VERSION} \
    conda-forge::r-biocmanager \
    conda-forge::r-xgboost=1.7.6=cpu_r43had0c348_6 \
    && micromamba clean --all --yes


