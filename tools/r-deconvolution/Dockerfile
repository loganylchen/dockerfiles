# PAIR M6A Biomarker - Immune Deconvolution Analysis
# Extends Bioconductor Docker image with immunedeconv and related tools
FROM bioconductor/bioconductor_docker:release_3.19

# Install R packages for immune cell deconvolution
RUN R -e "BiocManager::install(c( \
    'immunedeconv', \
    'ggplot2', \
    'pheatmap', \
    'RColorBrewer', \
    'gridExtra', \
    'corrplot', \
    'reshape2', \
    'tidyverse' \
    ), ask=FALSE, update=TRUE)"

# Install additional visualization packages
RUN R -e "install.packages(c( \
    'ggpubr', \
    'viridis', \
    'scales' \
    ), repos='https://cloud.r-project.org')"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
