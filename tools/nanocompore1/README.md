# Nanocompore 1.x RNA Modification Detection

**Category**: RNA Modification

## Introduction

RNA modification detection from Nanopore dRNA-seq (v1.x branch).

## Installation

```bash
docker pull btrspg/nanocompore1:1.0.4
```

## Available Versions

`1.0.4`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/nanocompore1 nanocompore1 --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/nanocompore1 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/nanocompore1 nanocompore1 [options]
```

## References

- [https://github.com/tlacombe/nanocompore](https://github.com/tlacombe/nanocompore)
