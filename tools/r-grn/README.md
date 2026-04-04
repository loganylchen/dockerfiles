# R-GRN Gene Regulatory Network

**Category**: Coexpression Network

## Introduction

Gene regulatory network inference and analysis.

## Installation

```bash
docker pull btrspg/r-grn:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/r-grn r-grn --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/r-grn bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/r-grn r-grn [options]
```

## References

