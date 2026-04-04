# CPAT Coding Potential Assessment

**Category**: Coding Potential

## Introduction

Predicts whether transcripts have protein-coding potential.

## Installation

```bash
docker pull btrspg/cpat:3.0.4
```

## Available Versions

`3.0.4`, `3.0.3`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/cpat cpat --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/cpat bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/cpat cpat [options]
```

## References

- [https://github.com/liguowang/cpat](https://github.com/liguowang/cpat)
