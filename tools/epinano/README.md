# EpiNano RNA Modification Analysis

**Category**: RNA Modification

## Introduction

Analyzes RNA modifications and sequence variants from Nanopore sequencing.

## Installation

```bash
docker pull btrspg/epinano:1.2.0
```

## Available Versions

`1.2.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/epinano epinano --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/epinano bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/epinano epinano [options]
```

## References

- [https://github.com/novoalab/EpiNano](https://github.com/novoalab/EpiNano)
