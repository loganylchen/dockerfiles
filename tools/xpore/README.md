# xPore Direct RNA Modification Detection

**Category**: RNA Modification

## Introduction

Identifies differential RNA modifications from direct RNA sequencing.

## Installation

```bash
docker pull btrspg/xpore:2.1
```

## Available Versions

`2.1`, `2.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/xpore xpore --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/xpore bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/xpore xpore [options]
```

## References

- [https://github.com/GoekeLab/xpore](https://github.com/GoekeLab/xpore)
