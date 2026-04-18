ARG VERSION=0.2.9

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="LeafCutter" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="LeafCutter - intron-centric splicing analysis and differential splicing" \
      org.opencontainers.image.source="https://github.com/davidaknowles/leafcutter" \
      org.opencontainers.image.licenses="Apache-2.0"

# Leafcutter R package is not on CRAN/Bioconductor; install from GitHub master.
# The 0.2.9 label matches the bioconda package (which versions the Python
# clustering scripts). Upstream GitHub max tag is v0.2.7, so use master HEAD.
# Strategy: use Debian pre-compiled r-cran-rstan/stanheaders/rstantools and
# r-bioc-dirichletmultinomial to avoid CRAN source compilation of rstan
# (historical cause of OOM and TBB issues).
RUN apt-get update && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        r-cran-rstan \
        r-cran-stanheaders \
        r-cran-rstantools \
        r-cran-foreach \
        r-cran-ggplot2 \
        r-cran-r.utils \
        r-cran-gridextra \
        r-cran-reshape2 \
        r-cran-hmisc \
        r-cran-dplyr \
        r-cran-domc \
        r-cran-optparse \
        r-cran-remotes \
        r-cran-biocmanager \
        r-bioc-dirichletmultinomial \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libgsl-dev \
        libfontconfig1-dev \
        zlib1g-dev \
        git \
        wget \
        ca-certificates \
        python3 \
        python3-pip \
        samtools \
    && Rscript -e "\
        options(repos=c(CRAN='https://cloud.r-project.org/')); \
        BiocManager::install('Biobase', ask=FALSE, update=FALSE); \
        install.packages('https://cloud.r-project.org/src/contrib/Archive/oompaBase/oompaBase_3.2.9.tar.gz', repos=NULL, type='source'); \
        install.packages('https://cloud.r-project.org/src/contrib/Archive/oompaData/oompaData_3.1.4.tar.gz', repos=NULL, type='source'); \
        install.packages('TailRank'); \
        remotes::install_github('davidaknowles/leafcutter/leafcutter', upgrade='never') \
    " \
    && git clone --depth 1 https://github.com/davidaknowles/leafcutter /opt/leafcutter \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && apt-get purge -y --auto-remove r-base-dev wget \
    && apt-get install -y --no-install-recommends libcurl4 \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

ENV PATH="/opt/leafcutter/clustering:/opt/leafcutter/scripts:${PATH}"

RUN Rscript -e "library(leafcutter); cat('leafcutter OK\n')"

WORKDIR /data
CMD ["Rscript"]
