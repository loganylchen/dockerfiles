# clusterProfiler Functional Enrichment Analysis

**Category**: Functional Annotation

## Introduction

R package for gene functional enrichment analysis and visualization (GO, KEGG, etc.).

## Installation

```bash
docker pull btrspg/clusterprofiler:4.12.6
```

## Available Versions

`4.12.6`, `4.10.1`, `4.8.3`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/clusterprofiler clusterprofiler --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/clusterprofiler bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/clusterprofiler clusterprofiler [options]
```

## References

- [https://bioconductor.org/packages/clusterProfiler/](https://bioconductor.org/packages/clusterProfiler/)
- Yu, G. et al. (2012). OMICS, 16(5), 284-287.
