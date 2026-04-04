# GffRead GFF/GTF Processing Tool

**Category**: Genomic Utilities

## Introduction

A tool for validating, filtering, and converting GFF/GTF annotation files.

## Installation

```bash
docker pull btrspg/gffread:0.12.7
```

## Available Versions

`0.12.7`, `0.12.6`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/gffread gffread --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/gffread bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/gffread gffread [options]
```

## References

- [http://ccb.jhu.edu/software/stringtie/gffread.shtml](http://ccb.jhu.edu/software/stringtie/gffread.shtml)
