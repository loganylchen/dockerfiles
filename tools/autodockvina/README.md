# AutoDock Vina Molecular Docking

**Category**: Protein Structure

## Introduction

Molecular docking software for computational drug discovery.

## Installation

```bash
docker pull btrspg/autodockvina:1.2.5
```

## Available Versions

`1.2.5`, `1.2.3`, `1.2.0`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/autodockvina autodockvina --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/autodockvina bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/autodockvina autodockvina [options]
```

## References

- [https://github.com/ccsb-scripps/AutoDock-Vina](https://github.com/ccsb-scripps/AutoDock-Vina)
