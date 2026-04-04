# FLAIR Transcript Annotation Tool

**Category**: RNA-seq Analysis

## Introduction

Full-length RNA isoform sequencing and annotation from long reads.

## Installation

```bash
docker pull btrspg/flair:2.0.0
```

## Available Versions

`2.0.0`, `1.7.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/flair flair --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/flair bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/flair flair [options]
```

## References

- [https://github.com/BrooksLabUCSC/flair](https://github.com/BrooksLabUCSC/flair)
