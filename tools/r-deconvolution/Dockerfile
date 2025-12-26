# PAIR M6A Biomarker - Immune Deconvolution Analysis
# Extends Bioconductor Docker image with immunedeconv and related tools
FROM bioconductor/bioconductor_docker:3.19

# Install R packages for immune cell deconvolution
RUN R -e "BiocManager::install(c( \
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
    'scales', \
    'devtools' \
    ), repos='https://cloud.r-project.org');\
    devtools::install_github('omnideconv/immunedeconv')"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
