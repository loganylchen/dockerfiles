# PAIR M6A Biomarker - Machine Learning Analysis
# Extends Bioconductor Docker image with glmnet, survival, and ML tools
FROM bioconductor/bioconductor_docker:release_3.19

# Install R packages for machine learning and survival analysis
RUN R -e "BiocManager::install(c( \
    'glmnet', \
    'survival', \
    'survminer', \
    'pROC', \
    'ggplot2', \
    'gridExtra', \
    'ComplexHeatmap' \
    ), ask=FALSE, update=TRUE)"

# Install additional ML and visualization packages from CRAN
RUN R -e "install.packages(c( \
    'caret', \
    'randomForest', \
    'xgboost', \
    'ggpubr', \
    'forestmodel', \
    'tidyverse', \
    'survivalROC', \
    'timeROC' \
    ), repos='https://cloud.r-project.org')"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
