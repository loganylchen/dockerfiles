# MAJIQ Alternative Splicing Quantification

**Category**: Alternative Splicing

## Introduction

Tool for detecting, quantifying, and visualizing local splicing variations from RNA-seq data.

## Installation

```bash
docker pull btrspg/majiq:2.5
```

## Available Versions

`2.5`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/majiq Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/majiq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/majiq majiq [options]
```

## References

- [https://majiq.biociphers.org/](https://majiq.biociphers.org/)
- Vaquero-Garcia, J. et al. (2016). eLife, 5, e11752.
