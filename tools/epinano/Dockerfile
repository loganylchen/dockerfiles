# Optimized Dockerfile for EpiNano v1.2.5
# EpiNano requires Python 3.6-3.7 and R for analysis scripts
# Based on README requirements: https://github.com/novoalab/EpiNano

FROM python:3.7-slim

ARG VERSION=1.2.5

LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="EpiNano - Detection of RNA modifications from Oxford Nanopore direct RNA sequencing"
LABEL version="${VERSION}"

# Set DEBIAN_FRONTEND to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # For downloading and extracting
    wget unzip \
    # Java for sam2tsv.jar (using openjdk-17 as openjdk-8 is deprecated)
    openjdk-17-jre-headless \
    # SAMtools for BAM processing
    samtools \
    # zlib and curl for Python packages
    zlib1g-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    # R for analysis scripts
    r-base \
    r-base-core \
    r-recommended \
    r-cran-ggplot2 \
    r-cran-optparse \
    r-cran-reshape2 \
    r-cran-car \
    r-cran-ggrepel \
    r-cran-stringr \
    r-cran-dplyr \
    r-cran-tidyr \
    r-cran-readr \
    r-cran-tibble \
    r-cran-purrr \
    r-cran-forcats \
    # Cleanup
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install R packages via CRAN (outliers is not available as apt package)
RUN R -e "install.packages(c('outliers'), repos='https://cloud.r-project.org/', dependencies=TRUE)"

# Download and install EpiNano using release zip (faster than git clone)
RUN wget -q https://github.com/novoalab/EpiNano/archive/refs/tags/EpiNano${VERSION}.zip -O epinano.zip && \
    unzip epinano.zip && \
    mv EpiNano-EpiNano${VERSION} /opt/epinano && \
    rm epinano.zip

# Patch EpiNano R scripts to use individual packages instead of tidyverse
RUN sed -i 's/suppressMessages (library(tidyverse))/suppressMessages(library(dplyr)); suppressMessages(library(tidyr)); suppressMessages(library(readr)); suppressMessages(library(tibble)); suppressMessages(library(stringr)); suppressMessages(library(ggplot2)); suppressMessages(library(purrr)); suppressMessages(library(forcats))/' /opt/epinano/Epinano_DiffErr.R && \
    sed -i 's/suppressMessages (library(tidyverse))/suppressMessages(library(dplyr)); suppressMessages(library(tidyr)); suppressMessages(library(readr)); suppressMessages(library(tibble)); suppressMessages(library(stringr)); suppressMessages(library(ggplot2)); suppressMessages(library(purrr)); suppressMessages(library(forcats))/' /opt/epinano/Epinano_Plot.R

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir \
    numpy==1.21.6 \
    pandas==1.3.5 \
    scipy==1.7.3 \
    scikit-learn==1.0.2 \
    biopython==1.79 \
    pysam==0.19.1 \
    h5py==3.7.0

# Add EpiNano to PATH
ENV PATH="/opt/epinano:$PATH"
ENV SAM2TSV="/opt/epinano/misc/sam2tsv.jar"

# Make Python scripts executable
RUN chmod +x /opt/epinano/*.py /opt/epinano/*.sh 2>/dev/null || true

# Set working directory
WORKDIR /data

# Verify installation
RUN python --version && \
    python -c "import numpy, pandas, scipy, sklearn, Bio, pysam, h5py; print('Python dependencies OK')" && \
    Rscript -e "library(dplyr); library(tidyr); library(readr); library(tibble); library(stringr); library(purrr); library(forcats); library(outliers); print('R packages OK')" && \
    samtools --version | head -1 && \
    java -version 2>&1 | head -1 && \
    Rscript --version && \
    echo "EpiNano scripts:" && \
    ls /opt/epinano/*.py | head -5

# Default command - show help
CMD ["python", "/opt/epinano/Epinano_Variants.py", "-h"]
