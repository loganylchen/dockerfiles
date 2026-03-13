ARG VERSION=0.5.0

# ── builder ──────────────────────────────────────────────────────────────────
FROM debian:bookworm-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        build-essential \
        cmake \
        gzip \
        libxml2-dev \
        zlib1g-dev \
        libeigen3-dev \
        libcairo2-dev \
        python3-dev \
        python3-pip \
        python3-rdkit \
        librdkit1 \
        rdkit-data \
    && rm -rf /var/lib/apt/lists/*

# Build OpenBabel 2.4.0 with Python bindings
RUN cd /tmp \
    && wget -q https://jaist.dl.sourceforge.net/project/openbabel/openbabel/2.4.0/openbabel-openbabel-2-4-0.tar.gz \
    && tar -xzf openbabel-openbabel-2-4-0.tar.gz \
    && mkdir build \
    && cd build \
    && cmake ../openbabel-openbabel-2-4-0 \
        -DPYTHON_BINDINGS=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/openbabel \
    && make -j$(nproc) \
    && make install \
    && rm -rf /tmp/*

# ── runtime ───────────────────────────────────────────────────────────────────
FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH=/opt/openbabel/bin:$PATH
ENV LD_LIBRARY_PATH=/opt/openbabel/lib:$LD_LIBRARY_PATH
ENV PYTHONPATH=/opt/openbabel/lib/python3:$PYTHONPATH

COPY --from=builder /opt/openbabel /opt/openbabel

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-rdkit \
        librdkit1 \
        rdkit-data \
        libxml2 \
        zlib1g \
        libcairo2 \
    && pip3 install --no-cache-dir --break-system-packages \
        numpy scipy pandas \
        meeko==${VERSION} \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -c "import meeko; print('meeko ok')"

WORKDIR /data
CMD ["python3"]
