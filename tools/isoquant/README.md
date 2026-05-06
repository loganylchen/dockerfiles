# IsoQuant

Reference-based analysis and quantification of long RNA reads (Oxford Nanopore
and PacBio) — transcript discovery, isoform assignment, and quantification.

- Source: https://github.com/ablab/IsoQuant
- Docs: https://ablab.github.io/IsoQuant
- License: GPL-2.0-only
- Default version: 3.13.0

## Build

```bash
docker build -t isoquant:3.13.0 --build-arg VERSION=3.13.0 .
```

## Run

```bash
docker run --rm -v $PWD:/data btrspg/isoquant:3.13.0 \
  isoquant \
    --reference /data/ref.fa \
    --genedb /data/annotation.gtf \
    --fastq /data/reads.fastq.gz \
    --data_type nanopore \
    --output /data/isoquant_out \
    --threads 8
```

## Notes

- Installed via PyPI: `pip install isoquant==3.13.0`
- Runtime includes `minimap2` and `samtools` for the alignment step (IsoQuant
  invokes them when given raw FASTQ).
- If you provide a pre-aligned BAM (`--bam`) you can skip those, but they're
  kept for the standard fastq-in workflow.
