# PUREE Alignment Filtering Tool

**Category**: RNA-seq Analysis

## Introduction

Purifies and filters RNA-seq alignments.

## Installation

```bash
docker pull btrspg/puree:5a0a702535e79e37b071971063e72fa697540818
```

## Available Versions

`5a0a702535e79e37b071971063e72fa697540818`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/puree puree --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/puree bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/puree puree [options]
```

## References

- [https://github.com/skandlab/PUREE](https://github.com/skandlab/PUREE)
