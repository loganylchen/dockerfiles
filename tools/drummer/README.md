# DRUMMER RNA Modification Analysis

**Category**: RNA Modification

## Introduction

Analyzes RNA modification patterns from RNA-seq alignments.

## Installation

```bash
docker pull btrspg/drummer:92bb35a4a2b22ff304f5e4bcbc9fa6985f18a12e
```

## Available Versions

`92bb35a4a2b22ff304f5e4bcbc9fa6985f18a12e`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/drummer drummer --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/drummer bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/drummer drummer [options]
```

## References

- [https://github.com/DepledgeLab/DRUMMER](https://github.com/DepledgeLab/DRUMMER)
