ARG VERSION=1.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

ENV PATH=/opt/bin:/opt/psinanopore:$PATH
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        libhdf5-dev libxml2-dev zlib1g-dev \
        wget git \
        r-base r-cran-ggplot2 r-cran-optparse \
    && rm -rf /var/lib/apt/lists/*

RUN Rscript -e 'install.packages(c("BiocManager"), repos="https://cran.r-project.org")' \
    && Rscript -e 'BiocManager::install(c("Biobase","Rsamtools","BSgenome"), ask=FALSE)' \
    && git clone --depth=1 https://github.com/RouhanifardLab/PsiNanopore.git /opt/psinanopore

COPY PsiDetect.R /opt/psinanopore/PsiDetect.R
COPY SignalView.R /opt/psinanopore/SignalView.R

RUN chmod +x /opt/psinanopore/*

WORKDIR /data
CMD ["bash"]
