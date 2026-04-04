# RNAseqLib RNA-seq Analysis Library

**Category**: Alternative Splicing

## Introduction

RNA-seq library for analyzing splicing patterns and creating gene annotations from GTF files.

## Installation

```bash
docker pull btrspg/rnaseqlib:1.1.2
```

## Available Versions

`1.1.2`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/rnaseqlib Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rnaseqlib bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rnaseqlib rnaseqlib [options]
```

## References

- [https://github.com/yarden/rnaseqlib](https://github.com/yarden/rnaseqlib)
