# NanoCount Long Read Quantification

**Category**: Transcript Quantification

## Introduction

Transcript abundance estimation for long-read sequencing.

## Installation

```bash
docker pull btrspg/nanocount:1.1.0.post2
```

## Available Versions

`1.1.0.post2`, `1.1.0`, `1.0.0.post6`, `1.0.0`

## Usage

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data btrspg/nanocount nanocount index -t transcripts.fa
docker run --rm -v /path/to/data:/data btrspg/nanocount nanocount quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/nanocount bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/nanocount nanocount [options]
```

## References

- [https://github.com/a-slide/NanoCount](https://github.com/a-slide/NanoCount)
