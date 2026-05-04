# TALON

TALON is a technology- and read-length-agnostic long-read analysis pipeline for the
identification and quantification of known and novel transcripts in long read
transcriptome data.

- Source: https://github.com/mortazavilab/TALON
- License: MIT
- Default version: 5.0

## Build

```bash
docker build -t talon:5.0 --build-arg VERSION=5.0 .
```

## Run

```bash
docker run --rm -v $PWD:/data talon:5.0 talon --help
```

## Notes

- TALON 5.0 requires Python `>=3.6,<3.8`; the image is built on
  `python:3.7-slim-bullseye` for that reason.
- `numpy` and `pandas` are pinned to versions that still support Python 3.7.
- All TALON CLI entry points are available on the PATH (`talon`,
  `talon_label_reads`, `talon_initialize_database`,
  `talon_filter_transcripts`, `talon_abundance`, `talon_create_GTF`,
  `talon_create_adata`, `talon_reformat_gtf`, `talon_generate_report`,
  `talon_summarize`, `talon_fetch_reads`, `talon_get_sjs`,
  `talon_longest_end`).
