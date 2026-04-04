# BEDTools Genomic Arithmetic Suite

**Category**: Genomic Utilities

## Introduction

A powerful toolset for genomic arithmetic operations on BED, BAM, VCF and other genomic file formats.

## Installation

```bash
docker pull btrspg/bedtools:2.31.1
```

## Available Versions

`2.31.1`, `2.31.0`, `2.30.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/bedtools bedtools --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/bedtools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/bedtools bedtools [options]
```

## References

- [https://bedtools.readthedocs.io/](https://bedtools.readthedocs.io/)
- Quinlan, A.R. & Hall, I.M. (2010). Bioinformatics, 26(6), 841-842.
