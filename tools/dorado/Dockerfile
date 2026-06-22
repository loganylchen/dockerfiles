ARG VERSION=2.0.1
ARG CUDA_VERSION=12.3.1

# nvidia/cuda base for GPU basecalling: it explicitly sets the NVIDIA env vars
# (NVIDIA_VISIBLE_DEVICES, NVIDIA_DRIVER_CAPABILITIES=compute,utility) and ships
# the CUDA runtime, so `--gpus all` reliably yields GPU compute regardless of the
# host container-toolkit defaults. Matches the repo's other GPU tools (bonito,
# directrm). dorado bundles its own CUDA libs, so the -runtime variant suffices.
FROM nvidia/cuda:${CUDA_VERSION}-runtime-ubuntu22.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ARG CUDA_VERSION

# Dorado ships as a precompiled linux-x64 tarball that bundles its own CUDA
# runtime libraries (rpath $ORIGIN/../lib); only the host NVIDIA driver is
# needed at runtime (run with `--gpus all`). No build toolchain required.
# The CDN publishes no checksums, so pin a SHA256 per supported version to
# detect tampering or silent CDN content changes (add a line here per version
# added to versions.txt).
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        libstdc++6 \
        zlib1g \
    && case "${VERSION}" in \
        2.0.1) SHA256=8b1eca77d4279142da97cebff051aa13a7d9a589a7517bf703c90fa7923ef5b6 ;; \
        1.4.0) SHA256=ea15250d911c6b6efdb21cc142008b2be8a5c781c8b0a4593b82f27b07385731 ;; \
        *) echo "No pinned SHA256 for dorado ${VERSION}" >&2; exit 1 ;; \
    esac \
    && wget -q -O /tmp/dorado.tar.gz \
        "https://cdn.oxfordnanoportal.com/software/analysis/dorado-${VERSION}-linux-x64.tar.gz" \
    && echo "${SHA256}  /tmp/dorado.tar.gz" | sha256sum -c - \
    && tar -xzf /tmp/dorado.tar.gz -C /opt \
    && mv "/opt/dorado-${VERSION}-linux-x64" /opt/dorado \
    && rm -f /tmp/dorado.tar.gz \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/* /tmp/*

ENV PATH=/opt/dorado/bin:${PATH}

RUN dorado --version

# Pre-bake the RNA004 (direct-RNA) sup@v5.3.0 simplex model plus the full set of
# modification models (inosine/m6A/2'O-meA, pseU/2'O-meU, m5C/2'O-meC, 2'O-meG,
# m6A_DRACH) into a fixed directory so RNA004 modified-basecalling needs no
# network at runtime. v5.3.0 is the newest RNA004 sup series available on every
# dorado version in versions.txt (1.4.0, 2.0.1). dorado has no models-directory
# env var; DORADO_MODELS_DIR is an image-level convention only. At runtime reuse
# the baked models via `--models-directory "$DORADO_MODELS_DIR"` (or pass a model
# path directly, e.g. "$DORADO_MODELS_DIR/rna004_130bps_sup@v5.3.0").
ENV DORADO_MODELS_DIR=/opt/dorado-models
RUN set -eux; \
    mkdir -p "${DORADO_MODELS_DIR}"; \
    SIMPLEX="rna004_130bps_sup@v5.3.0"; \
    for M in \
        "${SIMPLEX}" \
        "${SIMPLEX}_inosine_m6A_2OmeA@v1" \
        "${SIMPLEX}_pseU_2OmeU@v1" \
        "${SIMPLEX}_m5C_2OmeC@v1" \
        "${SIMPLEX}_2OmeG@v1" \
        "${SIMPLEX}_m6A_DRACH@v1" ; \
    do dorado download --model "$M" --models-directory "${DORADO_MODELS_DIR}"; done; \
    ls -1 "${DORADO_MODELS_DIR}"

WORKDIR /data
CMD ["dorado"]
