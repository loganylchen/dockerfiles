# Leafcutter Intron Splicing Analysis

**Category**: Alternative Splicing

## Introduction

Lightweight tool for quantifying and testing differential intron usage as a proxy for splicing.

## Installation

```bash
docker pull btrspg/leafcutter:0.2.9
```

## Available Versions

`0.2.9`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/leafcutter Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/leafcutter bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/leafcutter leafcutter [options]
```

## References

- [https://github.com/davidaknowles/leafcutter](https://github.com/davidaknowles/leafcutter)
- Li, Y.I. et al. (2018). Nat Genet, 50, 151-158.
