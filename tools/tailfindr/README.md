# tailfindr

Alignment-free poly(A)/poly(T) tail length estimator for 1D Oxford Nanopore
RNA and DNA reads.

- Source: https://github.com/adnaniazi/tailfindr
- License: GPL-3
- Default version: 1.4

## Build

```bash
docker build -t tailfindr:1.4 --build-arg VERSION=1.4 .
```

## Run

```bash
docker run --rm -v $PWD:/data tailfindr:1.4 \
  Rscript -e "library(tailfindr); find_tails(fast5_dir='/data/fast5', save_dir='/data/out', csv_filename='tails.csv', num_cores=4)"
```

## Notes

- Installed via `remotes::install_github('adnaniazi/tailfindr', ref='v1.4')`
  (not on CRAN/Bioconductor).
- Bioconductor deps `Biostrings` and `Rsamtools` are pre-installed via
  BiocManager so the GitHub install doesn't need to fetch them again.
- HDF5 system library required by `hdf5r` is provided by `libhdf5-dev` at
  build time and `libhdf5-103-1` for runtime (kept by R itself).
