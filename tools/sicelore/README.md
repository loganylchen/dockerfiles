# SiCeLoRe Single Cell Long Reads

**Category**: RNA-seq Analysis

## Introduction

Single-cell transcriptome reconstruction from long reads.

## Installation

```bash
docker pull btrspg/sicelore:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/sicelore sicelore --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/sicelore bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/sicelore sicelore [options]
```

## References

- [https://github.com/ucagenomix/sicelore](https://github.com/ucagenomix/sicelore)
