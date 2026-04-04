# slow5tools SLOW5 Format Tools

**Category**: Nanopore Analysis

## Introduction

Tools for manipulating SLOW5 files from nanopore sequencing.

## Installation

```bash
docker pull btrspg/slow5tools:1.4.0
```

## Available Versions

`1.4.0`, `1.3.0`, `1.2.0`, `1.1.0`, `1.0.0`, `0.9.0`

## Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data btrspg/slow5tools slow5tools reads.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/slow5tools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/slow5tools slow5tools [options]
```

## References

- [https://github.com/hasindu2008/slow5tools](https://github.com/hasindu2008/slow5tools)
