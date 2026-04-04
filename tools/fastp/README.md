# fastp Fast Quality Control Tool

**Category**: Quality Control

## Introduction

Ultra-fast all-in-one FASTQ preprocessor with quality control, filtering, and trimming.

## Installation

```bash
docker pull btrspg/fastp:0.24.0
```

## Available Versions

`0.24.0`, `0.23.2`

## Usage

```bash
# Quality control
docker run --rm -v /path/to/data:/data btrspg/fastp fastp -i input.fq -o output.html
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/fastp bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/fastp fastp [options]
```

## References

- [https://github.com/OpenGene/fastp](https://github.com/OpenGene/fastp)
- Chen, S. et al. (2018). iMeta, e20.
