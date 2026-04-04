# RNA-m5C Methylation Analysis

**Category**: RNA Modification

## Introduction

Analyzes m5C methylation modifications in RNA from sequencing data.

## Installation

```bash
docker pull btrspg/rnam5c:409be6485bcdd160f6c57e386ef71ff3ecb8e2f6
```

## Available Versions

`409be6485bcdd160f6c57e386ef71ff3ecb8e2f6`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/rnam5c rnam5c --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rnam5c bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rnam5c rnam5c [options]
```

## References

- [https://www.nature.com/articles/s41594-019-0218-x](https://www.nature.com/articles/s41594-019-0218-x)
