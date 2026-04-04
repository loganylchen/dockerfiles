# Bonito Nanopore Basecaller

**Category**: Nanopore Analysis

## Introduction

GPU-accelerated basecaller for Oxford Nanopore sequencing data using neural networks.

## Installation

```bash
docker pull btrspg/bonito:0.8.1
```

## Available Versions

`0.8.1`, `0.7.3`, `0.6.2`

## Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data btrspg/bonito bonito reads.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/bonito bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/bonito bonito [options]
```

## References

- [https://github.com/nanoporetech/bonito](https://github.com/nanoporetech/bonito)
