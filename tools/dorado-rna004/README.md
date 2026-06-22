# Dorado RNA004 Direct-RNA Basecaller

**Category**: Nanopore Analysis

## Introduction

Builds on the dorado image with the RNA004 sup@v5.3.0 model set pre-baked (simplex plus inosine/m6A/2'O-meA, pseU/2'O-meU, m5C/2'O-meC, 2'O-meG, and m6A_DRACH modification models) for offline modified-basecalling of Nanopore Direct RNA Sequencing data.

## Installation

```bash
docker pull btrspg/dorado-rna004:5.3.0
```

## Available Versions

`5.3.0`

## Usage

```bash
# Process Nanopore data
docker run --rm -v /path/to/data:/data btrspg/dorado-rna004 dorado reads.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/dorado-rna004 bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/dorado-rna004 dorado [options]
```

## References

- [https://github.com/nanoporetech/dorado](https://github.com/nanoporetech/dorado)
