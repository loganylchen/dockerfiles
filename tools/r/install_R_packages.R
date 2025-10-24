#!/usr/bin/env Rscript
# Install required R packages for plotting and data manipulation
# Packages: ggplot2, dplyr, ggpubr, ggsci, tidyr, tibble


github_repos <- c("slowkow/ggrepel")    # e.g. c("username/repo", "org/pkg@v1.2.3")


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