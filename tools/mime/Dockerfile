FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/conda/bin:$PATH


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
    conda-forge::r-randomforest \
    && micromamba clean --all --yes

ADD ./install_R_packages.R /tmp/

RUN micromamba run -n base Rscript /tmp/install_R_packages.R 
RUN micromamba run -n base Rscript -e 'remotes::install_version('randomForestSRC', version = '2.9.3',repos='http://cran.us.r-project.org')'

