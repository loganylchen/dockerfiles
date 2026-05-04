# RATTLE

Reference-free reconstruction and quantification of transcriptomes from
Nanopore long-read sequencing.

- Source: https://github.com/comprna/RATTLE
- License: MIT
- Default version: 1.0

## Build

```bash
docker build -t rattle:1.0 --build-arg VERSION=1.0 .
```

## Run

```bash
docker run --rm -v $PWD:/data rattle:1.0 rattle cluster -i reads.fq -o .
```

## Notes

- Multi-stage build: SPOA submodule is built with cmake, then RATTLE binary
  with `make`. Final image carries only the stripped `rattle` binary plus
  zlib runtime.
