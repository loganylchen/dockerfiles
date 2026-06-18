ARG VERSION=2.0.1

FROM ubuntu:22.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

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

WORKDIR /data
CMD ["dorado"]
