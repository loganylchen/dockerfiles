# STAR RNA-seq Aligner

**Category**: Sequence Alignment

## Introduction

Ultrafast universal RNA-seq aligner with splice-aware alignment support.

## Installation

```bash
docker pull btrspg/star:2.7.11b
```

## Available Versions

`2.7.11b`, `2.7.10b`

## Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data btrspg/star star -t 4 reference.fa reads.fq > alignment.sam
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/star bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/star star [options]
```

## References

- [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
- Dobin, A. et al. (2013). Bioinformatics, 29(1), 15-21.
