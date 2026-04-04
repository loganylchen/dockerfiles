# Nanopolish Nanopore Data Analysis

**Category**: Nanopore Analysis

## Introduction

Signal-level analysis and variant calling for Oxford Nanopore sequencing data.

## Installation

```bash
docker pull btrspg/nanopolish:0.14.0
```

## Available Versions

`0.14.0`

## Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data btrspg/nanopolish nanopolish reads.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/nanopolish bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/nanopolish nanopolish [options]
```

## References

- [https://github.com/jts/nanopolish](https://github.com/jts/nanopolish)
