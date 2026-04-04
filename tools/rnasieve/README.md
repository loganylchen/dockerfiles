# RNAsieve Transcript Quantification

**Category**: Transcript Quantification

## Introduction

Fast filtering and quantification of RNA sequences.

## Installation

```bash
docker pull btrspg/rnasieve:latest
```

## Available Versions

`latest`

## Usage

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data btrspg/rnasieve rnasieve index -t transcripts.fa
docker run --rm -v /path/to/data:/data btrspg/rnasieve rnasieve quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/rnasieve bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/rnasieve rnasieve [options]
```

## References

