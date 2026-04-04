# SVA Batch Effect Removal

**Category**: Differential Expression

## Introduction

Surrogate variable analysis for removing batch effects.

## Installation

```bash
docker pull btrspg/sva:3.52.0
```

## Available Versions

`3.52.0`, `3.50.0`, `3.48.0`

## Usage

```bash
# Run differential expression analysis in R
docker run --rm -v /path/to/data:/data btrspg/sva Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/sva bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/sva sva [options]
```

## References

- [https://bioconductor.org/packages/sva/](https://bioconductor.org/packages/sva/)
