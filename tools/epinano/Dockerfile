ARG VERSION=1.2.5

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# EpiNano >= 1.2.4 removed the sam2tsv (Java) dependency
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        unzip \
        ca-certificates \
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

# Download EpiNano (codeload zip extracts to EpiNano-EpiNano${VERSION}/)
RUN wget -q https://github.com/novoalab/EpiNano/archive/refs/tags/EpiNano${VERSION}.zip -O /tmp/epinano.zip \
    && unzip /tmp/epinano.zip -d /tmp \
    && mv /tmp/EpiNano-EpiNano${VERSION} /opt/epinano \
    && rm -rf /tmp/*

ENV PATH="/opt/epinano:$PATH"
RUN chmod +x /opt/epinano/*.py /opt/epinano/*.sh 2>/dev/null || true

# Verify installation
RUN python3 -c "import numpy, pandas, sklearn, Bio, pysam, h5py, dask; print('Python dependencies OK')" \
    && Rscript -e "library(tidyverse); library(outliers); cat('R packages OK\n')" \
    && minimap2 --version \
    && samtools --version \
    && python3 /opt/epinano/Epinano_Variants.py -h > /dev/null && echo "Epinano_Variants OK"

WORKDIR /data
CMD ["python3", "/opt/epinano/Epinano_Variants.py", "-h"]
