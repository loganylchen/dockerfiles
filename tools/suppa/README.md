# SUPPA Splicing Variation Quantification

**Category**: Alternative Splicing

## Introduction

Analyzes and compares alternative splicing events.

## Installation

```bash
docker pull btrspg/suppa:2.3
```

## Available Versions

`2.3`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/suppa Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/suppa bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/suppa suppa [options]
```

## References

- [https://github.com/comprna/SUPPA](https://github.com/comprna/SUPPA)
