# seqtk

Fast, lightweight toolkit for processing sequences in FASTA/Q formats.

- Source: https://github.com/lh3/seqtk
- License: MIT
- Default version: 1.5

## Build

```bash
docker build -t seqtk:1.5 --build-arg VERSION=1.5 .
```

## Run

```bash
# Convert FASTQ to FASTA
docker run --rm -v $PWD:/data btrspg/seqtk:1.5 \
  seqtk seq -A /data/in.fq.gz > out.fa

# Subsample 10000 reads (seeded)
docker run --rm -v $PWD:/data btrspg/seqtk:1.5 \
  seqtk sample -s100 /data/in.fq.gz 10000 > sub.fq

# Trim low-quality bases
docker run --rm -v $PWD:/data btrspg/seqtk:1.5 \
  seqtk trimfq /data/in.fq.gz > trimmed.fq
```

## Notes

- Multi-stage build: gcc + zlib in builder, only `zlib1g` runtime.
- Single static binary at `/usr/local/bin/seqtk`, stripped.
