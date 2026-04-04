# DirectRM RNA Modification Detection

**Category**: RNA Modification

## Introduction

Detects RNA modifications from Nanopore dRNA-seq using deep learning.

## Installation

```bash
docker pull btrspg/directrm:1.0
```

## Available Versions

`1.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/directrm directrm --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/directrm bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/directrm directrm [options]
```

## References

- [https://github.com/yuxinPenny/DirectRM](https://github.com/yuxinPenny/DirectRM)
