# Builder stage: compile f5c from edparam branch
FROM debian:bookworm-slim AS builder

ARG VERSION=12e0ca7f7312bdd67968c7975b8035a59665bfcc

RUN apt-get update && apt-get install -y --no-install-recommends \
        libhdf5-dev zlib1g-dev git automake autoconf gcc g++ make libbz2-dev liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && git clone --recursive https://github.com/hasindu2008/f5c \
    && cd f5c \
    && git checkout ${VERSION} \
    && autoreconf --install \
    && scripts/install-hts.sh \
    && ./configure --disable-hdf5 \
    && make -j$(nproc) \
    && strip f5c

# Runtime stage
FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        zlib1g libbz2-1.0 liblzma5 libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /tmp/f5c/f5c /usr/local/bin/f5c

RUN f5c --version

WORKDIR /data
CMD ["f5c"]
