# ModTect RNA Modification Detection

**Category**: RNA Modification

## Introduction

Detects RNA modifications from Nanopore sequencing data.

## Installation

```bash
docker pull btrspg/modtect:1.7.5.1
```

## Available Versions

`1.7.5.1`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/modtect modtect --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/modtect bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/modtect modtect [options]
```

## References

- [https://github.com/ktan8/ModTect](https://github.com/ktan8/ModTect)
