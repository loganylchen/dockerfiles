# RNA-SeQC RNA-seq Quality Control

**Category**: Quality Control

## Introduction

Comprehensive quality control for RNA-seq experiments.

## Installation

```bash
docker pull btrspg/rnaseqc:2.4.2
```

## Available Versions

`2.4.2`, `2.4.1`

## Usage

```bash
# Quality control
docker run --rm -v /path/to/data:/data btrspg/rnaseqc rnaseqc -i input.fq -o output.html
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rnaseqc bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rnaseqc rnaseqc [options]
```

## References

- [https://github.com/getzlab/rnaseqc](https://github.com/getzlab/rnaseqc)
