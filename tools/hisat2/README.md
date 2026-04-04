# HISAT2 Hierarchical Indexing Aligner

**Category**: Sequence Alignment

## Introduction

Fast and sensitive alignment for mapping next-generation sequencing reads.

## Installation

```bash
docker pull btrspg/hisat2:2.2.1
```

## Available Versions

`2.2.1`

## Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data btrspg/hisat2 hisat2 -t 4 reference.fa reads.fq > alignment.sam
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/hisat2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/hisat2 hisat2 [options]
```

## References

- [https://daehwankimlab.github.io/hisat2/](https://daehwankimlab.github.io/hisat2/)
- Kim, D. et al. (2019). Nat Methods, 12, 357-360.
