FROM mambaorg/micromamba:1.5


ENV PATH "${PATH}:/opt/Epinano/:/opt/conda/bin/"
ENV LC_ALL=en_US.utf8
ENV LANG=en_US.utf8

ARG DEEPTOOLS_VERSION=3.1.3

USER root
WORKDIR /opt/

RUN /usr/bin/micromamba install -y -c conda-forge -c bioconda -n base deeptools=${DEEPTOOLS_VERSION} && \
    /usr/bin/micromamba clean --all --yes







