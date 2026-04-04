# R-Validation Result Validation

**Category**: Quality Control

## Introduction

Validation and reporting tools for bioanalysis.

## Installation

```bash
docker pull btrspg/r-validation:3.19
```

## Available Versions

`3.19`

## Usage

```bash
# Quality control
docker run --rm -v /path/to/data:/data btrspg/r-validation r-validation -i input.fq -o output.html
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/r-validation bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/r-validation r-validation [options]
```

## References

