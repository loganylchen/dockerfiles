# ASpli Alternative Splicing Analysis

**Category**: Alternative Splicing

## Introduction

R/Bioconductor package for analysis, detection, and quantification of alternative splicing events from RNA-seq data.

## Installation

```bash
docker pull btrspg/aspli:2.14.0
```

## Available Versions

`2.14.0`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/aspli Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/aspli bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/aspli aspli [options]
```

## References

- [https://bioconductor.org/packages/ASpli/](https://bioconductor.org/packages/ASpli/)
- Mancini, E. et al. (2021). Bioinformatics, 37(18), 2884-2891.
