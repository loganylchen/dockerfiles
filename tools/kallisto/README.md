# Kallisto Pseudo-aligner

**Category**: Transcript Quantification

## Introduction

Near-optimal RNA-Seq quantification using pseudoalignment for rapid transcript abundance estimation.

## Installation

```bash
docker pull btrspg/kallisto:0.52.0
```

## Available Versions

`0.52.0`, `0.51.1`, `0.50.1`, `0.48.0`

## Usage

```bash
# Index reference and quantify
docker run --rm -v /path/to/data:/data btrspg/kallisto kallisto index -t transcripts.fa
docker run --rm -v /path/to/data:/data btrspg/kallisto kallisto quant -i transcripts.idx -o output reads_1.fq reads_2.fq
```

## Examples

```bash
# Interactive shell
docker run --rm -it -v $(pwd):/data btrspg/kallisto bash

# Run with data volume
docker run --rm -v /path/to/data:/data btrspg/kallisto kallisto [options]
```

## References

- [https://pachterlab.github.io/kallisto/](https://pachterlab.github.io/kallisto/)
- Bray, N.L. et al. (2016). Nat Biotechnol, 34, 525-527.
