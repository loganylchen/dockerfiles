# limma Linear Models for Microarray

**Category**: Differential Expression

## Introduction

R package for analyzing gene expression data from microarrays and RNA-seq using linear models.

## Installation

```bash
docker pull btrspg/limma:3.60.4
```

## Available Versions

`3.60.4`, `3.58.1`, `3.56.2`

## Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data btrspg/limma Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/limma bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/limma limma [options]
```

## References

- [https://bioconductor.org/packages/limma/](https://bioconductor.org/packages/limma/)
- Ritchie, M.E. et al. (2015). Nucleic Acids Res, 43(7), e47.
