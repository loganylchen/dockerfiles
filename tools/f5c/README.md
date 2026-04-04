# f5c Nanopore Signal Processing

**Category**: Nanopore Analysis

## Introduction

Efficient Oxford Nanopore signal processing for event alignment and methylation detection.

## Installation

```bash
docker pull btrspg/f5c:1.6
```

## Available Versions

`1.6`, `1.5`, `1.4`, `1.3`, `1.2`, `1.1`

## Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data btrspg/f5c f5c reads.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/f5c bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/f5c f5c [options]
```

## References

- [https://github.com/hasindu2008/f5c](https://github.com/hasindu2008/f5c)
