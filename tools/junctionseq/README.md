# JunctionSeq Differential Junction Analysis

**Category**: Alternative Splicing

## Introduction

R/Bioconductor package for analyzing differential junction and exon usage from RNA-seq data.

## Installation

```bash
docker pull btrspg/junctionseq:1.26.0
```

## Available Versions

`1.26.0`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/junctionseq Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/junctionseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/junctionseq junctionseq [options]
```

## References

- [https://bioconductor.org/packages/JunctionSeq/](https://bioconductor.org/packages/JunctionSeq/)
- Hartley, S.W. & Mullikin, J.C. (2016). Nucleic Acids Res, 44(16), e127.
