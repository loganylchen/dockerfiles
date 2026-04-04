# DEXSeq Differential Exon Usage Analysis

**Category**: Alternative Splicing

## Introduction

R/Bioconductor package for testing differential exon usage in RNA-seq data.

## Installation

```bash
docker pull btrspg/dexseq:1.50.0
```

## Available Versions

`1.50.0`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/dexseq Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/dexseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/dexseq dexseq [options]
```

## References

- [https://bioconductor.org/packages/DEXSeq/](https://bioconductor.org/packages/DEXSeq/)
- Anders, S. et al. (2012). Genome Res, 22(10), 2008-2017.
