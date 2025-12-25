# PAIR M6A Biomarker - Differential Expression Analysis
# Extends Bioconductor Docker image with DESeq2, edgeR, limma
FROM bioconductor/bioconductor_docker:3.19

# Install additional R packages for DEG analysis
# These packages are typically available but we ensure they're installed
RUN R -e "BiocManager::install(c( \
    'DESeq2', \
    'edgeR', \
    'limma', \
    'apeglm', \
    'ashr', \
    'pheatmap', \
    'ggplot2', \
    'EnhancedVolcano', \
    'RColorBrewer', \
    'gridExtra' \
    ), ask=FALSE, update=TRUE)"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
