# R-Tumor-Purity Tumor Purity Analysis

**Category**: Cell Deconvolution

## Introduction

Estimates tumor purity and immune composition.

## Installation

```bash
docker pull btrspg/r-tumor-purity:1.0
```

## Available Versions

`1.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/r-tumor-purity r-tumor-purity --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/r-tumor-purity bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/r-tumor-purity r-tumor-purity [options]
```

## References

