# Biopython Biological Computation Tools

**Category**: Python Bio Tools

## Introduction

Python tools for biological computation including sequence analysis and structural biology.

## Installation

```bash
docker pull btrspg/biopython:1.84
```

## Available Versions

`1.84`, `1.83`, `1.82`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/biopython biopython --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/biopython bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/biopython biopython [options]
```

## References

- [https://biopython.org/](https://biopython.org/)
- Cock, P.J. et al. (2009). Bioinformatics, 25(11), 1422-1423.
