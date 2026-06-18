# Dorado Nanopore Basecaller

**Category**: Nanopore Analysis

## Introduction

Oxford Nanopore's official GPU-accelerated basecaller supporting simplex/duplex calling, modified base detection (m6A, m5C, inosine, pseU, 2'O-me, etc.), and poly(A) tail length estimation.

## Installation

```bash
docker pull btrspg/dorado:2.0.1
```

## Available Versions

`2.0.1`, `1.4.0`

## Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data btrspg/dorado dorado reads.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/dorado bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/dorado dorado [options]
```

## References

- [https://github.com/nanoporetech/dorado](https://github.com/nanoporetech/dorado)
