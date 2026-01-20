FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH
ARG VERSION=9a9f6ac89851bf631f9df3868b2fa624bed49df2


RUN micromamba install -y \
    conda-forge::patch \
    conda-forge::libprotobuf \
    conda-forge::protobuf \
    bioconda::bioconductor-gsva \
    bioconda::bioconductor-gseabase \
    bioconda::bioconductor-cancerclass \
    bioconda::bioconductor-mixomics \
    bioconda::bioconductor-sparrow \
    bioconda::bioconductor-sva \
    conda-forge::cmake \
    conda-forge::r-klar \
    conda-forge::opentelemetry-sdk \
    bioconda::bioconductor-complexheatmap \
    conda-forge::r-devtools \
    conda-forge::r-survminer \
    conda-forge::r-xgboost \
    && micromamba clean --all --yes

ADD ./install_R_packages.R /tmp/

RUN micromamba run -n base Rscript /tmp/install_R_packages.R ${VERSION}


