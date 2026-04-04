# Bisque Transcriptomic Deconvolution

**Category**: Cell Deconvolution

## Introduction

Reference-based cell type deconvolution from bulk RNA-seq.

## Installation

```bash
docker pull btrspg/bisque:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/bisque bisque --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/bisque bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/bisque bisque [options]
```

## References

- [https://github.com/cozygene/bisque](https://github.com/cozygene/bisque)
