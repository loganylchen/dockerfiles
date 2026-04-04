# Picard Sequence Data Processing Tools

**Category**: Variant Calling

## Introduction

Java tools for processing high-throughput sequencing data including sorting and duplicate marking.

## Installation

```bash
docker pull btrspg/picard:3.2.0
```

## Available Versions

`3.2.0`, `3.1.1`, `3.0.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/picard picard --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/picard bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/picard picard [options]
```

## References

- [https://broadinstitute.github.io/picard/](https://broadinstitute.github.io/picard/)
