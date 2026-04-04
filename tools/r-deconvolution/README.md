# R-Deconvolution Immune Deconvolution

**Category**: Cell Deconvolution

## Introduction

Bioconductor environment for immune cell deconvolution.

## Installation

```bash
docker pull btrspg/r-deconvolution:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/r-deconvolution r-deconvolution --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/r-deconvolution bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/r-deconvolution r-deconvolution [options]
```

## References

