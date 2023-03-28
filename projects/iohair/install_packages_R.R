install_packages <- c("BiocManager", "devtools", "languageserver","dplyr", "ggplot2", "circlize", "gridExtra", "ggtern", "scatterplot3d",  "statmod", "ggalt","IRkernel")
install.packages(install_packages)


devtools::install_github("yanlinlin82/ggvenn")
devtools::install_github("jokergoo/ComplexHeatmap")
devtools::install_github("YuLab-SMU/clusterProfiler")
devtools::install_github("GangLiLab/genekitr@v1.1.3")

BiocManager::install(c("edgeR", "DESeq2", "limma","EnhancedVolcano","PCAtools","MAST"))

IRkernel::installspec(name = 'iohair_R', displayname = 'R IOHAIR',user=FALSE)



