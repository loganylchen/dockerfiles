# dorado with the RNA004 (direct-RNA) sup model set pre-baked, for offline
# modified-basecalling of Nanopore Direct RNA Sequencing data. Builds on the
# plain `dorado` image (same CDN binary) and only adds the downloaded models,
# so no toolchain is needed. VERSION selects the RNA004 sup model series; each
# series is tied to a dorado release (e.g. v5.3.0 needs dorado 1.4.0, v6.0.0
# would need dorado >= 2.x), so the matching dorado base is pinned per series.
ARG VERSION=5.3.0
ARG DORADO_VERSION=1.4.0

FROM btrspg/dorado:${DORADO_VERSION}
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION
ARG DORADO_VERSION

# Pre-download the RNA004 sup@v<VERSION> simplex model plus the full set of
# modification models (inosine/m6A/2'O-meA, pseU/2'O-meU, m5C/2'O-meC, 2'O-meG,
# m6A_DRACH) into a fixed directory so basecalling needs no network at runtime.
# dorado has no models-directory env var; DORADO_MODELS_DIR is an image-level
# convention only. At runtime, reuse the baked models by passing
# `--models-directory "$DORADO_MODELS_DIR"` (or give the model path directly,
# e.g. "$DORADO_MODELS_DIR/rna004_130bps_sup@v5.3.0").
ENV DORADO_MODELS_DIR=/opt/dorado-models
RUN set -eux; \
    case "${VERSION}" in \
        5.3.0) MODS_VERSION=v1 ;; \
        *) echo "Unsupported RNA004 model series ${VERSION}: pin a compatible dorado base (DORADO_VERSION) and mod-model suffix here" >&2; exit 1 ;; \
    esac; \
    mkdir -p "${DORADO_MODELS_DIR}"; \
    SIMPLEX="rna004_130bps_sup@v${VERSION}"; \
    for M in \
        "${SIMPLEX}" \
        "${SIMPLEX}_inosine_m6A_2OmeA@${MODS_VERSION}" \
        "${SIMPLEX}_pseU_2OmeU@${MODS_VERSION}" \
        "${SIMPLEX}_m5C_2OmeC@${MODS_VERSION}" \
        "${SIMPLEX}_2OmeG@${MODS_VERSION}" \
        "${SIMPLEX}_m6A_DRACH@${MODS_VERSION}" ; \
    do dorado download --model "$M" --models-directory "${DORADO_MODELS_DIR}"; done; \
    ls -1 "${DORADO_MODELS_DIR}"

WORKDIR /data
CMD ["dorado"]
