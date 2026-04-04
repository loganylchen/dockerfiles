# Meeko Molecular Preparation Tool

**Category**: Protein Structure

## Introduction

Prepares molecular structures for automated docking workflows.

## Installation

```bash
docker pull btrspg/meeko:0.7.1
```

## Available Versions

`0.7.1`, `0.5.0`, `0.4.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/meeko meeko --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/meeko bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/meeko meeko [options]
```

## References

- [https://github.com/forlilab/meeko](https://github.com/forlilab/meeko)
