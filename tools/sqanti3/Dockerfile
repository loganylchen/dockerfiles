# Thin overlay over the upstream SQANTI3 image. The upstream ships its Python
# dependencies (biopython, pandas, minimap2, samtools, gmap) inside a conda env
# named `sqanti3` and exposes them ONLY through the Docker ENTRYPOINT
# (`conda run -n sqanti3 ...`). Under Apptainer `exec` (how Snakemake runs it) the
# Docker ENTRYPOINT is ignored, so `sqanti3_qc.py` (#!/usr/bin/env python) runs
# under the base interpreter and fails with `ModuleNotFoundError: No module named
# 'Bio'`. Working around it with `conda run` in the rule is fragile: Apptainer
# passes the host environment through, and a host `conda init` exports a `conda`
# shell function that hijacks the bare command and points it at a host path absent
# in the container.
#
# This overlay fixes it once, in the image: put the `sqanti3` env bin on PATH so
# the right python/minimap2/samtools/gmap resolve with no wrapper, and clear the
# ENTRYPOINT so callers invoke `sqanti3_qc.py` directly.
ARG VERSION=6.0.1

FROM anaconesalab/sqanti3:v${VERSION}
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

LABEL org.opencontainers.image.title="SQANTI3" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="SQANTI3 long-read isoform structural classification/QC (Apptainer-friendly overlay: sqanti3 conda env on PATH, no ENTRYPOINT)" \
      org.opencontainers.image.source="https://github.com/ConesaLab/SQANTI3" \
      org.opencontainers.image.licenses="GPL-3.0"

# Prepend the upstream `sqanti3` conda env so Bio/pandas/minimap2/samtools/gmap
# resolve without `conda run`; clear the ENTRYPOINT for direct CLI invocation.
ENV PATH="/conda/miniconda3/envs/sqanti3/bin:${PATH}"
ENTRYPOINT []

# Fail the build if the env is not actually wired up.
RUN python -c "import Bio, pandas" \
    && which minimap2 samtools gmap sqanti3_qc.py \
    && sqanti3_qc.py --version

WORKDIR /data
CMD ["sqanti3_qc.py", "--help"]
