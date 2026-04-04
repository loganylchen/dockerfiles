# HAMR High-throughput RNA Modification Detection

**Category**: RNA Modification

## Introduction

Detects and quantifies RNA modifications using high-throughput sequencing.

## Installation

```bash
docker pull btrspg/hamr:latest
```

## Available Versions

`latest`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/hamr hamr --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/hamr bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/hamr hamr [options]
```

## References

- [https://github.com/GregoryLab/HAMR](https://github.com/GregoryLab/HAMR)
