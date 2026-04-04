# SRA Toolkit Sequence Data Download Tools

**Category**: Data Download

## Introduction

Tools for downloading and processing high-throughput sequencing data from NCBI Sequence Read Archive.

## Installation

```bash
docker pull btrspg/sratools:3.1.1
```

## Available Versions

`3.1.1`, `3.0.10`, `3.0.7`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/sratools sratools --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/sratools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/sratools sratools [options]
```

## References

- [https://github.com/ncbi/sra-tools](https://github.com/ncbi/sra-tools)
