# LIQA

Long-read Isoform Quantification and Analysis — EM-based isoform expression
estimation and differential alternative splicing for long-read RNA-seq.

- Source: https://github.com/WGLab/LIQA
- License: MIT
- Default version: 1.3.4

## Build

```bash
docker build -t liqa:1.3.4 --build-arg VERSION=1.3.4 .
```

## Run

```bash
# Step 1: preprocess the reference
docker run --rm -v $PWD:/data btrspg/liqa:1.3.4 \
  liqa -task refgene -ref /data/anno.gtf -format gtf -out /data/refgene.tsv

# Step 2: quantify isoform expression
docker run --rm -v $PWD:/data btrspg/liqa:1.3.4 \
  liqa -task quantify \
       -refgene /data/refgene.tsv \
       -bam /data/sample.bam \
       -out /data/sample.isoform_expression \
       -max_distance 10 -f_weight 1
```

## Notes

- Python deps installed via pip: `pysam`, `numpy`, `scipy`, `lifelines`.
- R deps installed from CRAN: `gcmr`, `betareg` (used in differential analysis).
- Tasks: `refgene`, `quantify`, `diff`, `novel`.
