# SpliceTools Splicing Tools Suite

**Category**: Alternative Splicing

## Introduction

Tools for analyzing RNA splice sites and junctions.

## Installation

```bash
docker pull btrspg/splicetools:latest
```

## Available Versions

`latest`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/splicetools Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/splicetools bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/splicetools splicetools [options]
```

## References

