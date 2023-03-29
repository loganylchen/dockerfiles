install_packages <- c("BiocManager","languageserver", "devtools", "dplyr", "ggplot2", "circlize", "gridExtra", "ggtern", "scatterplot3d", "Seurat", "statmod", "ggalt","IRkernel")
install.packages(install_packages)


devtools::install_github("yanlinlin82/ggvenn")
devtools::install_github("jokergoo/ComplexHeatmap")
devtools::install_github("neurorestore/Libra")
devtools::install_github("YuLab-SMU/clusterProfiler")
devtools::install_github("immunogenomics/presto")
devtools::install_github("kassambara/survminer", build_vignettes = FALSE)
BiocManager::install(c("edgeR", "DESeq2", "limma","EnhancedVolcano","PCAtools","MAST"))

IRkernel::installspec(name = 'BC_R', displayname = 'R BC',user=FALSE)



