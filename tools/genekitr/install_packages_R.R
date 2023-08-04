install_packages <- c("BiocManager", "devtools", "dplyr","geneset",'ggplot2','ggfun', 'cowplot')
install.packages(install_packages)
print('Install YuLab-SMU/ggtree')
devtools::install_github('YuLab-SMU/ggtree')
print('Install clusterProfiler')
BiocManager::install('clusterProfiler')
print('Install GangLiLab/genekitr')
devtools::install_github("GangLiLab/genekitr")



