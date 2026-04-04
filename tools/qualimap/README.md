# QualiMap Quality Assessment Tool

**Category**: Quality Control

## Introduction

Platform-independent application for quality control of alignment sequencing data.

## Installation

```bash
docker pull btrspg/qualimap:2.3
```

## Available Versions

`2.3`, `2.2.2d`

## Usage

```bash
# Quality control
docker run --rm -v /path/to/data:/data btrspg/qualimap qualimap -i input.fq -o output.html
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/qualimap bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/qualimap qualimap [options]
```

## References

- [http://qualimap.conesalab.org/](http://qualimap.conesalab.org/)
