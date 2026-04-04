# EnsemblDB Gene Annotation Database

**Category**: Functional Annotation

## Introduction

R/Bioconductor package for Ensembl genomic feature databases.

## Installation

```bash
docker pull btrspg/ensembldb:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/ensembldb ensembldb --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/ensembldb bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/ensembldb ensembldb [options]
```

## References

- [https://bioconductor.org/packages/ensembldb/](https://bioconductor.org/packages/ensembldb/)
