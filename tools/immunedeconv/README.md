# ImmuneDeconv Immune Cell Deconvolution

**Category**: Cell Deconvolution

## Introduction

Deconvolution of immune cell populations from transcriptomic data.

## Installation

```bash
docker pull btrspg/immunedeconv:2.1.0
```

## Available Versions

`2.1.0`, `2.0.3`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/immunedeconv immunedeconv --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/immunedeconv bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/immunedeconv immunedeconv [options]
```

## References

- [https://github.com/omnideconv/immunedeconv](https://github.com/omnideconv/immunedeconv)
