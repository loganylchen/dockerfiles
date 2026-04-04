# GeniON Gene Fusion Detection

**Category**: Gene Fusion

## Introduction

Fast sequence variant and gene fusion detection tool.

## Installation

```bash
docker pull btrspg/genion:1.1.1
```

## Available Versions

`1.1.1`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/genion genion --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/genion bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/genion genion [options]
```

## References

- [https://github.com/vpc-ccg/genion](https://github.com/vpc-ccg/genion)
