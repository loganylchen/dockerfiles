install_packages <- c("BiocManager", "devtools", "dplyr", "ggplot2", "circlize", "gridExtra", "ggtern", "scatterplot3d", "Seurat", "statmod", "ggalt","IRkernel")
install.packages(install_packages, repos = "https://mirror-hk.koddos.net/CRAN/")


devtools::install_github("yanlinlin82/ggvenn")
devtools::install_github("jokergoo/ComplexHeatmap")
devtools::install_github("neurorestore/Libra")
devtools::install_github("YuLab-SMU/clusterProfiler")
devtools::install_github("immunogenomics/presto")

BiocManager::install(c("edgeR", "DESeq2", "limma","EnhancedVolcano","PCAtools","MAST"))

IRkernel::installspec(name = 'BC_R', displayname = 'R BC')



