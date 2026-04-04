# HMMER Sequence Search Tools

**Category**: Genomic Utilities

## Introduction

Hidden Markov Model tools for protein and nucleotide sequence analysis.

## Installation

```bash
docker pull btrspg/hmmer:3.4
```

## Available Versions

`3.4`, `3.3.2`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/hmmer hmmer --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/hmmer bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/hmmer hmmer [options]
```

## References

- [https://eddylab.org/software/hmmer/](https://eddylab.org/software/hmmer/)
