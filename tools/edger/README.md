# edgeR Differential Expression Analysis

**Category**: Differential Expression

## Introduction

R package for differential expression analysis of RNA-seq data, especially suited for small sample sizes.

## Installation

```bash
docker pull btrspg/edger:4.2.1
```

## Available Versions

`4.2.1`, `4.0.16`, `3.42.4`

## Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data btrspg/edger Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/edger bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/edger edger [options]
```

## References

- [https://bioconductor.org/packages/edgeR/](https://bioconductor.org/packages/edgeR/)
- Robinson, M.D. et al. (2010). Bioinformatics, 26(1), 139-140.
