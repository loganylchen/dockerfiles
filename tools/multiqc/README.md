# MultiQC Quality Control Report Aggregator

**Category**: Quality Control

## Introduction

Aggregate results from multiple bioinformatics tools into a single HTML report.

## Installation

```bash
docker pull btrspg/multiqc:1.24.1
```

## Available Versions

`1.24.1`, `1.21`, `1.19`

## Usage

```bash
# Quality control
docker run --rm -v /path/to/data:/data btrspg/multiqc multiqc -i input.fq -o output.html
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/multiqc bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/multiqc multiqc [options]
```

## References

- [https://multiqc.info/](https://multiqc.info/)
- Ewels, P. et al. (2016). Bioinformatics, 32(19), 3047-3048.
