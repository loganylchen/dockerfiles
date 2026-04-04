# SCADEN Deep Learning Deconvolution

**Category**: Cell Deconvolution

## Introduction

Cell type deconvolution using deep learning with single-cell reference.

## Installation

```bash
docker pull btrspg/scaden:1.1.2
```

## Available Versions

`1.1.2`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/scaden scaden --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/scaden bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/scaden scaden [options]
```

## References

- [https://github.com/KevinMenden/scaden](https://github.com/KevinMenden/scaden)
