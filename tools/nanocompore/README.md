# Nanocompore RNA Modification Comparison

**Category**: RNA Modification

## Introduction

Detects differential RNA modifications from direct RNA-seq.

## Installation

```bash
docker pull btrspg/nanocompore:2.2.0
```

## Available Versions

`2.2.0`, `2.0.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/nanocompore nanocompore --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/nanocompore bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/nanocompore nanocompore [options]
```

## References

- [https://github.com/tlacombe/nanocompore](https://github.com/tlacombe/nanocompore)
