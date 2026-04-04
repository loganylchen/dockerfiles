# GLORI-tools Genomic Analysis Tools

**Category**: RNA Modification

## Introduction

Tools for genomic and transcriptomic analysis pipelines.

## Installation

```bash
docker pull btrspg/gloritools:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/gloritools gloritools --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/gloritools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/gloritools gloritools [options]
```

## References

- [https://github.com/liucongcas/GLORI-tools](https://github.com/liucongcas/GLORI-tools)
