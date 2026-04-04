# JAFFA Gene Fusion Detection

**Category**: Gene Fusion

## Introduction

Detects gene fusion events from RNA-seq data.

## Installation

```bash
docker pull btrspg/jaffal:2.3
```

## Available Versions

`2.3`, `2.2`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/jaffal jaffal --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/jaffal bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/jaffal jaffal [options]
```

## References

- [https://github.com/Oshlack/JAFFA](https://github.com/Oshlack/JAFFA)
