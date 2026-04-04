# GeneKitr Gene Functional Analysis

**Category**: Functional Annotation

## Introduction

Functional enrichment and visualization for genomic analysis.

## Installation

```bash
docker pull btrspg/genekitr:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/genekitr genekitr --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/genekitr bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/genekitr genekitr [options]
```

## References

- [https://github.com/GangLiLab/genekitr](https://github.com/GangLiLab/genekitr)
