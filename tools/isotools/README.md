# IsoTools

Framework for the analysis of long-read transcriptome sequencing data.

- Source: https://github.com/MatthiasLienhard/isotools
- License: MIT
- Default version: 0.3.4

## Build

```bash
docker build -t isotools:0.3.4 --build-arg VERSION=0.3.4 .
```

## Run

```bash
docker run --rm -v $PWD:/data isotools:0.3.4 run_isotools --help
```
