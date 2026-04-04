# Bambu Transcript Assembly Tool

**Category**: RNA-seq Analysis

## Introduction

Isoform discovery and quantification from long-read RNA-seq data.

## Installation

```bash
docker pull btrspg/bambu:3.4.0
```

## Available Versions

`3.4.0`, `3.2.6`, `3.0.8`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/bambu bambu --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/bambu bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/bambu bambu [options]
```

## References

- [https://bioconductor.org/packages/bambu/](https://bioconductor.org/packages/bambu/)
