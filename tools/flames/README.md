# FLAMES

Full-Length Analysis of Mutations and Splicing in long-read RNA-seq —
semi-supervised isoform detection, annotation, and quantification for both
bulk and single-cell long-read RNA-seq.

- Source: https://github.com/mritchielab/FLAMES
- Docs: https://mritchielab.github.io/FLAMES
- License: GPL-3.0-or-later
- Default version: 2.4.2 (Bioconductor 3.22 release)

## Build

```bash
docker build -t flames:2.4.2 --build-arg VERSION=2.4.2 .
```

## Run

```bash
docker run --rm -v $PWD:/data btrspg/flames:2.4.2 \
  Rscript -e 'library(FLAMES); ?bulk_long_pipeline'
```

## Notes

- Installed via `BiocManager::install('FLAMES')` against Bioconductor 3.22.
- Pulls in heavy deps: `bambu`, `BiocParallel`, `ShortRead`, `Rsamtools`,
  `scater`, `scran`, `ComplexHeatmap`, `ggbio`, `magick`, plus `Rcpp`/`Rhtslib`
  (compiled from source against the bundled htslib).
- `basilisk` manages a private conda env for the Python-side helpers — it is
  **not** pre-warmed in this image; the first call into a basilisk-backed
  function will materialise it (needs network on first run).
- Build is large (≈3-4 GB during install) and slow (~30 min on a clean cache).
