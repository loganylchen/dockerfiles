# WGCNA Weighted Gene Coexpression

**Category**: Coexpression Network

## Introduction

Weighted gene coexpression network analysis.

## Installation

```bash
docker pull btrspg/wgcna:1.73
```

## Available Versions

`1.73`, `1.72_5`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/wgcna wgcna --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/wgcna bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/wgcna wgcna [options]
```

## References

- [https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/](https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/)
