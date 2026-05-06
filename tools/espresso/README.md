# ESPRESSO

Error Statistics PRomoted Evaluator of Splice Site Options — long-read RNA-seq
splice junction correction and isoform quantification.

- Source: https://github.com/Xinglab/espresso
- License: BSD-2-Clause
- Default version: 1.6.0

## Build

```bash
docker build -t espresso:1.6.0 --build-arg VERSION=1.6.0 .
```

## Run

ESPRESSO is a 3-step pipeline (S, C, Q):

```bash
docker run --rm -v $PWD:/data btrspg/espresso:1.6.0 \
  perl /opt/espresso/src/ESPRESSO_S.pl \
    -L /data/samples.tsv -F /data/ref.fa -A /data/anno.gtf -O /data/out
```

The included Snakemake workflow at `/opt/espresso/snakemake/` is NOT installed
here (it relies on conda). Run the three Perl scripts directly:

- `ESPRESSO_S.pl` — splice junction calling
- `ESPRESSO_C.pl` — error correction
- `ESPRESSO_Q.pl` — quantification

## Notes

- Built on `debian:bookworm-slim` (system perl 5.36 with thread support and
  `Storable >= 3.15`).
- Multi-stage build: bundled Parasail Perl XS module is compiled against
  jeffdaily/parasail v2.6.2 in the builder, then copied into the runtime.
- Runtime tools: `hmmer`, `ncbi-blast+`, `samtools`, `minimap2`, plus
  `python3` + `numpy` for visualization scripts.
- UCSC `bedGraphToBigWig` / `faToTwoBit` / `twoBitInfo` are NOT bundled — add
  them separately if you need the full visualization pipeline.
