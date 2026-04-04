# SignalP Signal Peptide Prediction

**Category**: Protein Structure

## Introduction

Predicts signal peptides in protein sequences.

## Installation

```bash
docker pull btrspg/signalp:5.0b
```

## Available Versions

`5.0b`

## Usage

```bash
# Basic usage
docker run --rm -v /path/to/data:/data btrspg/signalp signalp --help
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/signalp bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/signalp signalp [options]
```

## References

- [https://services.healthtech.dtu.dk/services/SignalP-5.0/](https://services.healthtech.dtu.dk/services/SignalP-5.0/)
