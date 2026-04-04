# MGLTools Molecular Visualization Suite

**Category**: Protein Structure

## Introduction

Molecular graphics and computational tools for protein structure analysis.

## Installation

```bash
docker pull btrspg/mgltools:1.5.7
```

## Available Versions

`1.5.7`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/mgltools mgltools --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/mgltools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/mgltools mgltools [options]
```

## References

- [https://ccsb.scripps.edu/mgltools/](https://ccsb.scripps.edu/mgltools/)
