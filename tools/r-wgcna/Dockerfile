# PAIR M6A Biomarker - Validation Analysis
# Extends Bioconductor Docker image with validation and reporting tools
FROM bioconductor/bioconductor_docker:3.19

# Install R packages for validation and report generation
RUN R -e "BiocManager::install(c( \
    'rmarkdown', \
    'knitr', \
    'corrplot', \
    'ggplot2', \
    'pheatmap', \
    'RColorBrewer', \
    'gridExtra', \
    'ComplexHeatmap', \
    'circlize', \
    'DESeq2', \
    'glmnet', \
    'survival', \
    'pROC' \
    ), ask=FALSE, update=TRUE)"

# Install additional packages from CRAN
RUN R -e "install.packages(c( \
    'ggpubr', \
    'tidyr', \
    'dplyr', \
    'flextable', \
    'kableExtra', \
    'DT' \
    ), repos='https://cloud.r-project.org')"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
