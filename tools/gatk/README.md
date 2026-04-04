# GATK Genome Analysis Toolkit

**Category**: Variant Calling

## Introduction

Comprehensive toolkit for variant discovery and genotyping, widely used in human genomics research.

## Installation

```bash
docker pull btrspg/gatk:4.6.1.0
```

## Available Versions

`4.6.1.0`, `4.5.0.0`, `4.4.0.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/gatk gatk --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/gatk bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/gatk gatk [options]
```

## References

- [https://gatk.broadinstitute.org/](https://gatk.broadinstitute.org/)
- Van der Auwera, G.A. et al. (2013). Curr Protoc Bioinformatics, 43, 11.10.1-11.10.33.
