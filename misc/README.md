# misc images

Date-tagged base images for R and Python. A new image is built automatically whenever
the corresponding `Dockerfile` or package list changes. The tag format is `YYYY-MM-DD`.

---

## python3

**Image:** `${DH_USER}/misc-python3:<date>`  
**Base:** `ubuntu:22.04`

| Package | Description |
|---------|-------------|
| pandas | DataFrame library |
| numpy | Numerical computing |
| matplotlib | Plotting |
| seaborn | Statistical visualization |
| scikit-learn | Machine learning |
| scipy | Scientific computing |
| bx-python | Biological sequence analysis |

### Build history

<!-- PYTHON3_HISTORY -->
| 2026-03-26 | packages: pandas,numpy,matplotlib,seaborn,scikit-learn,scipy,bx-python,statsmodels,tqdm |
| 2026-03-26 | packages: pandas,numpy,matplotlib,seaborn,scikit-learn,scipy,bx-python,statsmodels |
| Date | Notes |
|------|-------|
<!-- /PYTHON3_HISTORY -->

---

## r-base

**Image:** `${DH_USER}/misc-r-base:<date>`  
**Base:** `debian:bookworm-slim`

| Package | Source | Description |
|---------|--------|-------------|
| tidyverse | CRAN | Data manipulation and wrangling |
| ggplot2 | CRAN | Grammar of graphics plotting |
| ggpubr | CRAN | Publication-ready ggplot2 figures |
| ggsci | CRAN | Scientific journal color palettes |
| ggrepel | CRAN | Non-overlapping text labels |
| ggalt | CRAN | Extra ggplot2 geoms |
| ggplotify | CRAN | Convert plots to ggplot objects |
| patchwork | CRAN | Compose multiple plots |
| pheatmap | CRAN | Pretty heatmaps |
| UpSetR | CRAN | UpSet plots |
| dplyr | CRAN | Data manipulation |
| tidyr | CRAN | Tidy data |
| tibble | CRAN | Modern data frames |
| readr | CRAN | Fast file reading |
| devtools | CRAN | Package development tools |
| magick | CRAN | Image processing |
| BiocManager | CRAN | Bioconductor package manager |
| ComplexHeatmap | Bioconductor | Advanced heatmaps |
| EnhancedVolcano | Bioconductor | Volcano plots |
| PCAtools | Bioconductor | PCA analysis |
| DESeq2 | Bioconductor | Differential expression analysis |
| linkET | GitHub (Hy4m/linkET) | Linkage and correlation heatmaps |

### Build history

<!-- RBASE_HISTORY -->
| Date | Notes |
|------|-------|
<!-- /RBASE_HISTORY -->
