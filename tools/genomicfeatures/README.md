# GenomicFeatures Genomic Feature Tools

**Category**: Functional Annotation

## Introduction

R/Bioconductor tools for genomic features and annotations.

## Installation

```bash
docker pull btrspg/genomicfeatures:1.62.0
```

## Available Versions

`1.62.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/genomicfeatures genomicfeatures --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/genomicfeatures bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/genomicfeatures genomicfeatures [options]
```

## References

- [https://bioconductor.org/packages/GenomicFeatures/](https://bioconductor.org/packages/GenomicFeatures/)
