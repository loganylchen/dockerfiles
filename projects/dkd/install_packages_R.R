install_packages <- c("BiocManager", "devtools","languageserver", "dplyr", "ggplot2", "circlize", "gridExtra", "ggtern", "scatterplot3d", "Seurat", "statmod", "ggalt","IRkernel","ggpubr")
install.packages(install_packages)

devtools::install_github('YuLab-SMU/ggtree')
BiocManager::install('clusterProfiler')
BiocManager::install('org.Hs.eg.db')
devtools::install_github("GangLiLab/genekitr@v1.1.3")

devtools::install_github("yanlinlin82/ggvenn")
devtools::install_github("jokergoo/ComplexHeatmap")
devtools::install_github("neurorestore/Libra")
devtools::install_github("immunogenomics/presto")

BiocManager::install(c("edgeR", "DESeq2", "limma","EnhancedVolcano","PCAtools","MAST"))

IRkernel::installspec(name = 'DKD_R', displayname = 'R DKD',user=FALSE)



