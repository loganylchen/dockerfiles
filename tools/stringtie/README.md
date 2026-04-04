# StringTie Transcript Assembler

**Category**: RNA-seq Analysis

## Introduction

A fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.

## Installation

```bash
docker pull btrspg/stringtie:2.2.3
```

## Available Versions

`2.2.3`, `2.2.1`, `2.1.7`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/stringtie stringtie --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/stringtie bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/stringtie stringtie [options]
```

## References

- [https://ccb.jhu.edu/software/stringtie/](https://ccb.jhu.edu/software/stringtie/)
- Pertea, M. et al. (2015). Nat Biotechnol, 33, 290-295.
