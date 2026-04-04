# IsoformSwitchAnalyzeR Isoform Switch Analysis

**Category**: Alternative Splicing

## Introduction

Analyzes functional consequences of isoform switches.

## Installation

```bash
docker pull btrspg/isoformswitchanalyzer:2.4.0
```

## Available Versions

`2.4.0`, `2.2.0`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/isoformswitchanalyzer Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/isoformswitchanalyzer bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/isoformswitchanalyzer isoformswitchanalyzer [options]
```

## References

- [https://bioconductor.org/packages/IsoformSwitchAnalyzeR/](https://bioconductor.org/packages/IsoformSwitchAnalyzeR/)
