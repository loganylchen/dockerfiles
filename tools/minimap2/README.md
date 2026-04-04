# Minimap2 Long Read Aligner

**Category**: Sequence Alignment

## Introduction

A versatile pairwise aligner for genomic and spliced nucleotide sequences, optimized for long reads (PacBio/Oxford Nanopore).

## Installation

```bash
docker pull btrspg/minimap2:2.30
```

## Available Versions

`2.30`, `2.29`, `2.28`, `2.27`, `2.26`, `2.25`

## Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data btrspg/minimap2 minimap2 -t 4 reference.fa reads.fq > alignment.sam
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/minimap2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/minimap2 minimap2 [options]
```

## References

- [https://github.com/lh3/minimap2](https://github.com/lh3/minimap2)
- Li, H. (2018). Bioinformatics, 34(18), 3094-3100.
