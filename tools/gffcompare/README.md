# GffCompare Annotation Comparison Tool

**Category**: RNA-seq Analysis

## Introduction

Compare and evaluate transcript assemblies against reference annotations.

## Installation

```bash
docker pull btrspg/gffcompare:0.12.10
```

## Available Versions

`0.12.10`, `0.12.9`, `0.12.6`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/gffcompare gffcompare --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/gffcompare bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/gffcompare gffcompare [options]
```

## References

- [https://ccb.jhu.edu/software/stringtie/gffcompare.shtml](https://ccb.jhu.edu/software/stringtie/gffcompare.shtml)
