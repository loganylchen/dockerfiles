# Subread Sequence Alignment Tool

**Category**: Sequence Alignment

## Introduction

High-performance read alignment and feature counting tool, includes featureCounts.

## Installation

```bash
docker pull btrspg/subread:2.0.6
```

## Available Versions

`2.0.6`, `2.0.3`

## Usage

```bash
# Basic alignment
docker run --rm -v /path/to/data:/data btrspg/subread subread -t 4 reference.fa reads.fq > alignment.sam
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/subread bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/subread subread [options]
```

## References

- [http://subread.sourceforge.net/](http://subread.sourceforge.net/)
- Liao, Y. et al. (2013). Nucleic Acids Res, 41(10), e108.
