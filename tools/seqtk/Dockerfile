ARG VERSION=1.5

FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
        zlib1g-dev \
    && wget -q "https://github.com/lh3/seqtk/archive/refs/tags/v${VERSION}.tar.gz" -O /tmp/seqtk.tar.gz \
    && tar -xzf /tmp/seqtk.tar.gz -C /tmp \
    && cd /tmp/seqtk-${VERSION} \
    && make -j$(nproc) \
    && strip seqtk \
    && install -m 0755 seqtk /usr/local/bin/seqtk

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="seqtk" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="seqtk - toolkit for processing sequences in FASTA/Q formats" \
      org.opencontainers.image.source="https://github.com/lh3/seqtk" \
      org.opencontainers.image.licenses="MIT"

RUN apt-get update && apt-get install -y --no-install-recommends \
        zlib1g \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/seqtk /usr/local/bin/seqtk

RUN seqtk 2>&1 | head -3

WORKDIR /data
CMD ["seqtk"]
