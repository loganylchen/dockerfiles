# Salmon Transcript Quantifier

**Category**: Transcript Quantification

## Introduction

Fast and bias-aware quantification of transcript expression using selective alignment.

## Installation

```bash
docker pull btrspg/salmon:1.11.4
```

## Available Versions

`1.11.4`, `1.10.0`, `1.9.0`

## Usage

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data btrspg/salmon salmon index -t transcripts.fa
docker run --rm -v /path/to/data:/data btrspg/salmon salmon quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/salmon bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/salmon salmon [options]
```

## References

- [https://github.com/COMBINE-lab/salmon](https://github.com/COMBINE-lab/salmon)
- Patro, R. et al. (2017). Nat Methods, 14, 417-419.
