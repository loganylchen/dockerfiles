install_packages <- c("BiocManager", "devtools", "dplyr","geneset",'ggplot2')
install.packages(install_packages)

devtools::install_github('YuLab-SMU/ggtree')
BiocManager::install('clusterProfiler')
devtools::install_github("GangLiLab/genekitr")



