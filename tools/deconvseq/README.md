# DeconvSeq Deconvolution Analysis

**Category**: Cell Deconvolution

## Introduction

Immune cell deconvolution from RNA-seq data.

## Installation

```bash
docker pull btrspg/deconvseq:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/deconvseq deconvseq --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/deconvseq bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/deconvseq deconvseq [options]
```

## References

- [https://github.com/rosedu1/deconvSeq](https://github.com/rosedu1/deconvSeq)
