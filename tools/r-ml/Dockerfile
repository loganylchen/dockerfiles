# PAIR M6A Biomarker - Gene Regulatory Network Analysis
# Extends Bioconductor Docker image with GENIE3, minet, and network tools
FROM bioconductor/bioconductor_docker:3.19

# Install R packages for gene regulatory network inference
RUN R -e "BiocManager::install(c( \
    'GENIE3', \
    'minet', \
    'igraph', \
    'ggraph', \
    'ggplot2', \
    'pheatmap', \
    'RColorBrewer', \
    'gridExtra' \
    ), ask=FALSE, update=TRUE)"

# Install additional packages from CRAN
RUN R -e "install.packages(c( \
    'visNetwork', \
    'networkD3', \
    'tidyverse' \
    ), repos='https://cloud.r-project.org')"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
