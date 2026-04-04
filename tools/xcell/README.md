# xCell Cell Type Scoring

**Category**: Cell Deconvolution

## Introduction

Infers immune and stromal cell types from gene expression data.

## Installation

```bash
docker pull btrspg/xcell:1.1.0
```

## Available Versions

`1.1.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/xcell xcell --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/xcell bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/xcell xcell [options]
```

## References

- [https://xcell.ucsf.edu/](https://xcell.ucsf.edu/)
