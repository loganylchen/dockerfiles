# TidyEstimate Tumor Estimation Tool

**Category**: Cell Deconvolution

## Introduction

Tidy interface to ESTIMATE for tumor purity analysis.

## Installation

```bash
docker pull btrspg/tidyestimate:1.1.1
```

## Available Versions

`1.1.1`, `1.0.4`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/tidyestimate tidyestimate --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/tidyestimate bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/tidyestimate tidyestimate [options]
```

## References

- [https://github.com/KaiAragaki/tidyestimate](https://github.com/KaiAragaki/tidyestimate)
