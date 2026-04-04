ARG VERSION=0.24.0

FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        g++ make git ca-certificates zlib1g-dev libisal-dev libdeflate-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth=1 --branch v${VERSION} https://github.com/OpenGene/fastp.git /tmp/fastp \
    && cd /tmp/fastp \
    && make -j$(nproc) \
    && strip fastp

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        zlib1g libisal2 libdeflate0 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /tmp/fastp/fastp /usr/local/bin/fastp

RUN fastp --version 2>&1

WORKDIR /data
CMD ["fastp"]
