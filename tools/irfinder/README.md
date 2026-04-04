# IRFinder Intron Retention Detector

**Category**: Alternative Splicing

## Introduction

Tool for detecting and quantifying intron retention events from RNA-seq data.

## Installation

```bash
docker pull btrspg/irfinder:2.0.1
```

## Available Versions

`2.0.1`

## Usage

```bash
# Run alternative splicing analysis
docker run --rm -v /path/to/data:/data btrspg/irfinder Rscript analysis.R
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/irfinder bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/irfinder irfinder [options]
```

## References

- [https://github.com/RitchieLabIGH/IRFinder](https://github.com/RitchieLabIGH/IRFinder)
- Middleton, R. et al. (2017). Genome Res, 27(10), 1726-1737.
