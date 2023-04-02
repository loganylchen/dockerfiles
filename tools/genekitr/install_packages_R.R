install_packages <- c("BiocManager", "devtools", "dplyr","geneset")
install.packages(install_packages)

BiocManager::install("ggtree")

devtools::install_github("YuLab-SMU/clusterProfiler")
devtools::install_github("GangLiLab/genekitr@v1.1.3")



