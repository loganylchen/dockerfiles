# IUPred2a Protein Disorder Prediction

**Category**: Protein Structure

## Introduction

Predicts intrinsically disordered regions in proteins.

## Installation

```bash
docker pull btrspg/iupred2a:2a
```

## Available Versions

`2a`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/iupred2a iupred2a --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/iupred2a bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/iupred2a iupred2a [options]
```

## References

- [https://iupred.elte.hu/](https://iupred.elte.hu/)
