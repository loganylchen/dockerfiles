ARG VERSION=1.2.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# EpiNano v1.2.0 requires Java (sam2tsv.jar bundled in misc/)
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        unzip \
        ca-certificates \
        default-jre-headless \
        python3 \
        python3-pip \
        r-base \
        r-cran-tidyverse \
        r-cran-optparse \
        r-cran-reshape2 \
        r-cran-car \
        r-cran-ggrepel \
        r-cran-stringr \
        minimap2 \
        samtools \
    && Rscript -e "install.packages('outliers', repos='https://cloud.r-project.org/')" \
    && pip3 install --no-cache-dir --break-system-packages \
        'numpy>=1.26' \
        'pandas>=1.5' \
        'scikit-learn>=1.3' \
        'biopython>=1.83' \
        'pysam>=0.22' \
        'h5py>=3.10' \
        'dask>=2024.2' \
        'pyarrow' \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache /tmp/Rtmp*

# Symlink python -> python3 for EpiNano shebangs
RUN ln -s /usr/bin/python3 /usr/bin/python

# Download EpiNano v1.2.0 (sam2tsv.jar bundled in misc/)
RUN wget -q https://github.com/novoalab/EpiNano/archive/refs/tags/Epinano${VERSION}.zip -O /tmp/epinano.zip \
    && unzip /tmp/epinano.zip -d /tmp \
    && mv /tmp/EpiNano-Epinano${VERSION} /opt/epinano \
    && rm -rf /tmp/*

ENV PATH="/opt/epinano:$PATH"
ENV SAM2TSV="/opt/epinano/misc/sam2tsv.jar"
RUN chmod +x /opt/epinano/*.py /opt/epinano/*.sh 2>/dev/null || true

# Verify installation
RUN python3 -c "import numpy, pandas, sklearn, Bio, pysam, h5py, dask; print('Python dependencies OK')" \
    && Rscript -e "library(tidyverse); library(outliers); cat('R packages OK\n')" \
    && minimap2 --version \
    && samtools --version \
    && java -version 2>&1 \
    && test -f /opt/epinano/misc/sam2tsv.jar && echo "sam2tsv.jar OK"

WORKDIR /data
CMD ["python3", "/opt/epinano/Epinano_Variants.py", "-h"]
