# R-WGCNA Weighted Coexpression Environment

**Category**: Coexpression Network

## Introduction

Weighted gene coexpression network analysis and enrichment environment.

## Installation

```bash
docker pull btrspg/r-wgcna:3.19
```

## Available Versions

`3.19`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/r-wgcna r-wgcna --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/r-wgcna bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/r-wgcna r-wgcna [options]
```

## References

