FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y -c conda-forge -c bioconda bioconductor-bambu=${VERSION} \
    conda-forge::r-biocmanager \
    && Rscript -e "install.packages('xgboost')" \
    && micromamba clean --all --yes


