# Differr RNA Modification Detection

**Category**: RNA Modification

## Introduction

Detects differentially modified RNA sites from direct RNA-seq data.

## Installation

```bash
docker pull btrspg/differr:0.2
```

## Available Versions

`0.2`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/differr differr --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/differr bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/differr differr [options]
```

## References

- [https://github.com/bartongroup/differr_nanopore_DRS](https://github.com/bartongroup/differr_nanopore_DRS)
