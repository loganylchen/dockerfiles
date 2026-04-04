# ESTIMATE Tumor Purity Estimation

**Category**: Cell Deconvolution

## Introduction

Estimates stromal and immune content in tumor samples.

## Installation

```bash
docker pull btrspg/estimate:1.0.13
```

## Available Versions

`1.0.13`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/estimate estimate --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/estimate bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/estimate estimate [options]
```

## References

- [https://r-forge.r-project.org](https://r-forge.r-project.org)
