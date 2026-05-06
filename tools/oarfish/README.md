# oarfish

Transcript-level quantification from long-read RNA-seq (Oxford Nanopore /
PacBio). Fast, written in Rust.

- Source: https://github.com/COMBINE-lab/oarfish
- License: BSD-3-Clause
- Default version: 0.9.4

## Build

```bash
docker build -t oarfish:0.9.4 --build-arg VERSION=0.9.4 .
```

## Run

```bash
docker run --rm -v $PWD:/data btrspg/oarfish:0.9.4 \
  oarfish \
    --alignments /data/aligned.bam \
    --output /data/oarfish_out \
    --threads 8
```

## Notes

- Uses the upstream prebuilt `x86_64-unknown-linux-gnu` binary (mostly static).
- No extra runtime deps — minimap2/samtools should be done outside the
  container if you need to align reads first.
