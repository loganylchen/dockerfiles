#!/usr/bin/env Rscript
# Install required R packages for plotting and data manipulation
# Packages: ggplot2, dplyr, ggpubr, ggsci, tidyr, tibble

pkgs <- c("BiocManager","ggplot2", "dplyr", "ggpubr", "ggsci", "tidyr", "tibble","devtools")
bioc_pkgs <- c('PCAtools')       # e.g. c("GenomicFeatures", "Biostrings")
github_repos <- c("slowkow/ggrepel")    # e.g. c("username/repo", "org/pkg@v1.2.3")

options(repos = c(CRAN = "https://cloud.r-project.org"))


# Install with dependencies; use multiple CPUs if available
ncpus <- tryCatch(parallel::detectCores(), error = function(e) 1L)
tryCatch(
    install.packages(pkgs,  dependencies = TRUE, Ncpus = ncpus),
    error = function(e) {
        message("Installation failed: ", conditionMessage(e))
        quit(status = 1)
    }
)





tryCatch(
    BiocManager::install(bioc_pkgs, ask = FALSE, update = FALSE, Ncpus = ncpus),
    error = function(e) {
        message("Bioconductor installation failed: ", conditionMessage(e))
        quit(status = 1)
    }
)

    




for (repo in github_repos) {
    tryCatch(
        {
            devtools::install_github(repo, dependencies = TRUE, upgrade = "never",)
            message("Installed GitHub repo: ", repo)
        },
        error = function(e) {
            message("Failed to install GitHub repo ", repo, ": ", conditionMessage(e))
            quit(status = 1)
        }
    )
}


message("All requested packages installed.")