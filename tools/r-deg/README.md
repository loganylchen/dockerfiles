# R-DEG Differential Expression Environment

**Category**: Differential Expression

## Introduction

Bioconductor environment for differential expression analysis.

## Installation

```bash
docker pull btrspg/r-deg:latest
```

## Available Versions

`latest`

## Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data btrspg/r-deg Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/r-deg bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/r-deg r-deg [options]
```

## References

