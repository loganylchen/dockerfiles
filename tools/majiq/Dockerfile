ARG VERSION=2.4.0

FROM continuumio/miniconda3
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

RUN conda install -y -c bioconda -c conda-forge \
        majiq=${VERSION} \
    && conda clean -afy \
    && rm -rf /tmp/* /root/.cache

RUN majiq --version

WORKDIR /data
CMD ["majiq"]
