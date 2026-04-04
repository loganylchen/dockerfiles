# LAFITE Full-length Isoform Clustering

**Category**: Alternative Splicing

## Introduction

Full-length isoform clustering from Nanopore direct RNA-seq.

## Installation

```bash
docker pull btrspg/lafite:1.0.2
```

## Available Versions

`1.0.2`, `1.0.1`, `1.0.0`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/lafite Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/lafite bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/lafite lafite [options]
```

## References

- [https://github.com/pythseq/LAFITE](https://github.com/pythseq/LAFITE)
