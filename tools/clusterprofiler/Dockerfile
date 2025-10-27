FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION

RUN micromamba install -y \
    bioconda::bioconductor-clusterprofiler=${VERSION} \
    bioconda::bioconductor-dose \
    bioconda::bioconductor-org.hs.eg.db \
    bioconda::bioconductor-org.mm.eg.db \
    bioconda::bioconductor-deseq2 \
    && micromamba clean --all --yes




