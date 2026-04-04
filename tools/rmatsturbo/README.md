# rMATS-turbo Fast Splicing Analysis

**Category**: Alternative Splicing

## Introduction

High-performance alternative splicing event detection.

## Installation

```bash
docker pull btrspg/rmatsturbo:4.3.0
```

## Available Versions

`4.3.0`, `4.2.0`, `4.1.2`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/rmatsturbo Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rmatsturbo bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rmatsturbo rmatsturbo [options]
```

## References

- [https://github.com/Xinglab/rmats-turbo](https://github.com/Xinglab/rmats-turbo)
