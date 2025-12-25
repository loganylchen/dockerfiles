# PAIR M6A Biomarker - WGCNA Analysis
# Extends Bioconductor Docker image with WGCNA and enrichment tools
FROM bioconductor/bioconductor_docker:3.19

# Install R packages for WGCNA and functional enrichment
RUN R -e "BiocManager::install(c( \
    'WGCNA', \
    'clusterProfiler', \
    'org.Hs.eg.db', \
    'enrichplot', \
    'ggplot2', \
    'pheatmap', \
    'RColorBrewer', \
    'gridExtra', \
    'ComplexHeatmap', \
    'circlize', \
    'DOSE', \
    'ReactomePA', \
    'pathview' \
    ), ask=FALSE, update=TRUE)"

# Install org.Mm.eg.db for mouse datasets (optional)
RUN R -e "BiocManager::install('org.Mm.eg.db', ask=FALSE, update=TRUE)"

# Set working directory
WORKDIR /data

# Default command
CMD ["R"]
