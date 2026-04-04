# rMATS Alternative Splicing Quantification

**Category**: Alternative Splicing

## Introduction

Detects and quantifies alternative splicing events from RNA-seq data.

## Installation

```bash
docker pull btrspg/rmats:4.3.0
```

## Available Versions

`4.3.0`, `4.2.0`, `4.1.2`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/rmats Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rmats bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rmats rmats [options]
```

## References

- [https://rnaseq-mats.sourceforge.io/](https://rnaseq-mats.sourceforge.io/)
