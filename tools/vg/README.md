# VG Variation Graph Toolkit

**Category**: Pangenome

## Introduction

Tools for building and analyzing genome variation graphs with graph-based alignment.

## Installation

```bash
docker pull btrspg/vg:1.59.0
```

## Available Versions

`1.59.0`, `1.56.0`, `1.53.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/vg vg --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/vg bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/vg vg [options]
```

## References

- [https://github.com/vgteam/vg](https://github.com/vgteam/vg)
