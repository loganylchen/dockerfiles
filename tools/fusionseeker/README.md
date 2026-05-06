# FusionSeeker

Gene fusion caller for long-read transcriptome sequencing (PacBio Iso-Seq,
Oxford Nanopore).

- Source: https://github.com/Maggi-Chen/FusionSeeker
- License: MIT
- Default version: 1.0.1 (pinned to commit `d33b11b`, 2023-08-02 — has the
  `accept failed poa step` bugfix on top of tagged v1.0.1)

## Build

```bash
docker build -t fusionseeker:1.0.1 --build-arg VERSION=1.0.1 .
```

## Run

```bash
# Iso-Seq with bundled GRCh38 GTF
docker run --rm -v $PWD:/data btrspg/fusionseeker:1.0.1 \
  fusionseeker --bam /data/aligned.sort.bam \
               --datatype isoseq \
               --human38 \
               --ref /data/hg38.fa \
               --outpath /data/fs_out

# Custom reference
docker run --rm -v $PWD:/data btrspg/fusionseeker:1.0.1 \
  fusionseeker --bam /data/aligned.sort.bam \
               --datatype nanopore \
               --gtf /data/anno.gtf \
               --ref /data/genome.fa \
               --outpath /data/fs_out
```

## Notes

- Bundled `Homo_sapiens.GRCh37.87.chrname.gtf.gz` and
  `Homo_sapiens.GRCh38.104.chrname.gtf.gz` are at `/opt/fusionseeker/`
  (used when `--human19`/`--human38` is set).
- `bsalign` (required for breakpoint polishing) is built from
  github.com/ruanjue/bsalign and copied to `/usr/local/bin`.
- `pysam`, `minimap2`, `samtools` provided via Debian packages.
