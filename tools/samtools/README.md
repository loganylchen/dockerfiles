# Samtools Sequence Alignment Tools

**Category**: Genomic Utilities

## Introduction

Tools for manipulating next-generation sequencing data in SAM/BAM/CRAM formats.

## Installation

```bash
docker pull btrspg/samtools:1.23.1
```

## Available Versions

`1.23.1`, `1.22.2`, `1.21.1`, `1.19.1`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/samtools samtools --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/samtools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/samtools samtools [options]
```

## References

- [http://www.htslib.org/](http://www.htslib.org/)
