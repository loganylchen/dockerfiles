# SplAdder Alternative Splicing Detection

**Category**: Alternative Splicing

## Introduction

Tool for detecting, quantifying, and analyzing alternative splicing events from RNA-seq alignments.

## Installation

```bash
docker pull btrspg/spladder:3.0.4
```

## Available Versions

`3.0.4`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/spladder Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/spladder bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/spladder spladder [options]
```

## References

- [https://github.com/ratschlab/spladder](https://github.com/ratschlab/spladder)
- Kahles, A. et al. (2016). Bioinformatics, 32(12), i39-i48.
