# BEDOPS High-Performance Genomic Operations

**Category**: Genomic Utilities

## Introduction

High-performance genomic data operations suite optimized for large-scale genomic data analysis.

## Installation

```bash
docker pull btrspg/bedops:2.4.41
```

## Available Versions

`2.4.41`, `2.4.40`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/bedops bedops --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/bedops bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/bedops bedops [options]
```

## References

- [https://bedops.readthedocs.io/](https://bedops.readthedocs.io/)
