FROM mambaorg/micromamba:latest
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV PATH=/opt/bin:$PATH
ARG VERSION
USER micromamba
RUN micromamba install -y -c conda-forge -c bioconda flair=${VERSION} \
    && micromamba clean --all --yes


