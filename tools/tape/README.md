# TAPE Transcriptome Autoencoder

**Category**: Cell Deconvolution

## Introduction

Deep learning for single-cell transcriptomics.

## Installation

```bash
docker pull btrspg/tape:1.1.2
```

## Available Versions

`1.1.2`, `1.1.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/tape tape --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/tape bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/tape tape [options]
```

## References

- [https://github.com/poseidonchan/TAPE](https://github.com/poseidonchan/TAPE)
