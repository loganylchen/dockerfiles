# DESeq2 Differential Expression Analysis

**Category**: Differential Expression

## Introduction

R package for differential gene expression analysis based on the negative binomial distribution.

## Installation

```bash
docker pull btrspg/deseq2:1.44.0
```

## Available Versions

`1.44.0`, `1.42.1`, `1.40.2`

## Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data btrspg/deseq2 Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/deseq2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/deseq2 deseq2 [options]
```

## References

- [https://bioconductor.org/packages/DESeq2/](https://bioconductor.org/packages/DESeq2/)
- Love, M.I. et al. (2014). Genome Biol, 15, 550.
