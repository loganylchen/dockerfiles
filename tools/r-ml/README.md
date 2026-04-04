# R-ML Machine Learning Analysis

**Category**: Statistics / Machine Learning

## Introduction

Machine learning tools for genomic data analysis.

## Installation

```bash
docker pull btrspg/r-ml:3.19
```

## Available Versions

`3.19`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/r-ml r-ml --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/r-ml bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/r-ml r-ml [options]
```

## References

