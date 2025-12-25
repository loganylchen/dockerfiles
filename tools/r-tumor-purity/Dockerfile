# PAIR M6A Biomarker - Tumor Purity Analysis
# Extends Bioconductor Docker image with ESTIMATE and purity estimation tools
FROM bioconductor/bioconductor_docker:release_3.19

# Install R packages for tumor purity estimation
RUN R -e "BiocManager::install(c( \
    'estimate', \
    'immunedeconv', \
    'ggplot2', \
    'pheatmap', \
    'RColorBrewer', \
    'gridExtra', \
    'corrplot', \
    'ComplexHeatmap', \
    'circlize' \
    ), ask=FALSE, update=TRUE)"

# Install additional packages from CRAN
RUN R -e "install.packages(c( \
    'ggpubr', \
    'tidyverse', \
    'scales', \
    'viridis' \
    ), repos='https://cloud.r-project.org')"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
