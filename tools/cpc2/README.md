# CPC2 Coding Potential Classifier

**Category**: Coding Potential

## Introduction

Classifies sequences as protein-coding or non-coding.

## Installation

```bash
docker pull btrspg/cpc2:1.0.1
```

## Available Versions

`1.0.1`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/cpc2 cpc2 --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/cpc2 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/cpc2 cpc2 [options]
```

## References

- [https://github.com/gao-lab/CPC2_standalone](https://github.com/gao-lab/CPC2_standalone)
