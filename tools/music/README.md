# MuSiC Cell Type Deconvolution

**Category**: Cell Deconvolution

## Introduction

Bulk tissue deconvolution via single-cell transcriptomics.

## Installation

```bash
docker pull btrspg/music:1.0.0
```

## Available Versions

`1.0.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/music music --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/music bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/music music [options]
```

## References

- [https://github.com/xuranw/MuSiC](https://github.com/xuranw/MuSiC)
