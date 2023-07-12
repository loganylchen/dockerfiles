install_packages <- c("snowfall", "NMF")
bioc_packages <- c("BiocParallel","scran")
install.packages(install_packages)
BiocManager::install(bioc_packages)
install.extras('NMF')
devtools::install_github("Danko-Lab/BayesPrism/BayesPrism")




