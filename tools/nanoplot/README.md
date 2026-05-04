# NanoPlot

Plotting suite for Oxford Nanopore sequencing data and alignments.

- Source: https://github.com/wdecoster/NanoPlot
- License: MIT
- Default version: 1.42.0

## Build

```bash
docker build -t nanoplot:1.42.0 --build-arg VERSION=1.42.0 .
```

## Run

```bash
docker run --rm -v $PWD:/data nanoplot:1.42.0 NanoPlot --fastq input.fastq -o out
```
