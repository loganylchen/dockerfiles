# deepTools NGS Visualization

**Category**: Python Bio Tools

## Introduction

Python tools for analyzing and visualizing high-throughput sequencing data.

## Installation

```bash
docker pull btrspg/deeptools:3.5.6
```

## Available Versions

`3.5.6`, `3.5.5`, `3.5.3`, `3.5.2`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/deeptools deeptools --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/deeptools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/deeptools deeptools [options]
```

## References

- [https://deeptools.readthedocs.io/](https://deeptools.readthedocs.io/)
- Ramirez, F. et al. (2016). Nucleic Acids Res, 44(W1), W160-W165.
