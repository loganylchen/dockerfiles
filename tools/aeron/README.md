# AERON Gene Fusion Detection

**Category**: Gene Fusion

## Introduction

Transcript quantification and gene-fusion detection using long reads.

## Installation

```bash
docker pull btrspg/aeron:c77c73a4bdeb6fb21fa7522239b2276e27ea10f8
```

## Available Versions

`c77c73a4bdeb6fb21fa7522239b2276e27ea10f8`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/aeron aeron --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/aeron bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/aeron aeron [options]
```

## References

- [https://www.biorxiv.org/content/10.1101/2020.01.27.921338v1](https://www.biorxiv.org/content/10.1101/2020.01.27.921338v1)
