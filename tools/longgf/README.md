# LongGF Long Read Fusion Detection

**Category**: Gene Fusion

## Introduction

Generates gene fusion GTF files from long read BAM alignments.

## Installation

```bash
docker pull btrspg/longgf:0.1.2
```

## Available Versions

`0.1.2`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/longgf longgf --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/longgf bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/longgf longgf [options]
```

## References

- [https://github.com/WGLab/LongGF](https://github.com/WGLab/LongGF)
