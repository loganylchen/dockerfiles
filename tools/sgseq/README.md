# SGSeq Splice Graph Analysis

**Category**: Alternative Splicing

## Introduction

R/Bioconductor package for splice graph analysis of exon usage and splice site patterns from RNA-seq data.

## Installation

```bash
docker pull btrspg/sgseq:1.38.0
```

## Available Versions

`1.38.0`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/sgseq Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/sgseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/sgseq sgseq [options]
```

## References

- [https://bioconductor.org/packages/SGSeq/](https://bioconductor.org/packages/SGSeq/)
- Goldstein, L.D. et al. (2016). BMC Bioinformatics, 17, 464.
