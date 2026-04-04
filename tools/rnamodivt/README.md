# RNAModivt RNA Modification Integrated Analysis

**Category**: RNA Modification

## Introduction

Comprehensive pipeline for RNA modification analysis with systematic calibration.

## Installation

```bash
docker pull btrspg/rnamodivt:48df2c04ee063c96aaefde64df915a867528f93e
```

## Available Versions

`48df2c04ee063c96aaefde64df915a867528f93e`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/rnamodivt rnamodivt --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rnamodivt bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rnamodivt rnamodivt [options]
```

## References

- [https://www.nature.com/articles/s41592-021-01280-7](https://www.nature.com/articles/s41592-021-01280-7)
