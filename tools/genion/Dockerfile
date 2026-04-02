ARG VERSION=1.1.1

# ── builder ──────────────────────────────────────────────────────────────────
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        make \
        g++ \
        gcc \
        zlib1g-dev \
    && cd /tmp \
    && wget -q https://github.com/vpc-ccg/genion/archive/refs/tags/v${VERSION}.tar.gz \
    && tar -xzf v${VERSION}.tar.gz \
    && cd genion-${VERSION} \
    && make \
    && strip genion \
    && mv genion /usr/local/bin/genion \
    && rm -rf /var/lib/apt/lists/* /tmp/*

# ── runtime ───────────────────────────────────────────────────────────────────
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        zlib1g \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/genion /usr/local/bin/genion

RUN genion --version 2>&1 || genion --help 2>&1

WORKDIR /data
CMD ["genion"]
