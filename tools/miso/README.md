# MISO Mixture of Isoforms Analysis

**Category**: Alternative Splicing

## Introduction

Probabilistic framework for estimating percent-spliced-in (PSI) values of alternatively spliced exons from RNA-seq.

## Installation

```bash
docker pull btrspg/miso:0.5.4
```

## Available Versions

`0.5.4`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/miso Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/miso bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/miso miso [options]
```

## References

- [https://miso.readthedocs.io/](https://miso.readthedocs.io/)
- Katz, Y. et al. (2010). Nat Methods, 7(12), 1009-1015.
