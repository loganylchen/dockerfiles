# Whippet Fast Splicing Analysis

**Category**: Alternative Splicing

## Introduction

Fast Julia-based RNA-seq splicing analysis tool for quantifying percent-spliced-in (PSI) values.

## Installation

```bash
docker pull btrspg/whippet:1.6.1
```

## Available Versions

`1.6.1`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/whippet Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/whippet bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/whippet whippet [options]
```

## References

- [https://github.com/timbitz/Whippet.jl](https://github.com/timbitz/Whippet.jl)
- Sterne-Weiler, T. et al. (2018). Mol Cell, 72(1), 187-200.
