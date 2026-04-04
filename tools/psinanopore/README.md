# PsiNanopore Nanopore Splicing Analysis

**Category**: Alternative Splicing

## Introduction

Analyzes percent-spliced-in from Nanopore sequencing.

## Installation

```bash
docker pull btrspg/psinanopore:latest
```

## Available Versions

`latest`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/psinanopore Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/psinanopore bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/psinanopore psinanopore [options]
```

## References

- [https://github.com/RouhanifardLab/PsiNanopore](https://github.com/RouhanifardLab/PsiNanopore)
