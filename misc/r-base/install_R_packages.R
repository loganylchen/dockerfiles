#!/usr/bin/env Rscript
# Install required R packages for plotting and data manipulation
# Packages: ggplot2, dplyr, ggpubr, ggsci, tidyr, tibble

# The rocker/r-ver base preconfigures Posit PPM (with the correct HTTPUserAgent)
# to serve precompiled binaries for this R version, so we install against the
# inherited repos rather than overriding them. This avoids the fragile source
# build of the devtools -> miniUI -> shiny -> bslib chain on this distro.

install.packages(c(
            'BiocManager',
            'tidyverse',
            'ggplot2',
            'ggpubr',
            'ggsci',
            'ggrepel',
            'ggalt',
            'ggplotify',
            'patchwork',
            'pheatmap',
            'UpSetR',
            'dplyr',
            'tidyr',
            'tibble',
            'readr',
            'devtools',
            'magick',
            'readr'
        ))
  
BiocManager::install(c(
            'ComplexHeatmap',
            'EnhancedVolcano',
            'PCAtools',
            'DESeq2',
            'GenomicRanges',
            'rtracklayer',
            'GenomicFeatures'
        ), ask=FALSE)


github_repos <- c("Hy4m/linkET")    # e.g. c("username/repo", "org/pkg@v1.2.3")


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
