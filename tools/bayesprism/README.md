# BayesPrism Cell Type Deconvolution

**Category**: Cell Deconvolution

## Introduction

Bayesian cell type deconvolution from bulk RNA-seq data.

## Installation

```bash
docker pull btrspg/bayesprism:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/bayesprism bayesprism --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/bayesprism bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/bayesprism bayesprism [options]
```

## References

- [https://github.com/Danko-Lab/BayesPrism](https://github.com/Danko-Lab/BayesPrism)
