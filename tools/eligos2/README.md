# ELIGOS2 RNA Modification Identification

**Category**: RNA Modification

## Introduction

Identifies RNA modifications from direct RNA-seq data.

## Installation

```bash
docker pull btrspg/eligos2:2.1.0
```

## Available Versions

`2.1.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/eligos2 eligos2 --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/eligos2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/eligos2 eligos2 [options]
```

## References

- [https://gitlab.com/piroonj/eligos2](https://gitlab.com/piroonj/eligos2)
