# Builder stage: build samtools
FROM debian:bookworm-slim AS builder

ARG SAMTOOLS_VERSION=1.22.1

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget g++ make libncurses-dev zlib1g-dev libbz2-dev liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && tar -jxf samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && cd samtools-${SAMTOOLS_VERSION} \
    && ./configure --prefix=/usr/local \
    && make -j$(nproc) && make install \
    && strip /usr/local/bin/samtools

# Runtime stage
FROM ubuntu:20.04

ARG VERSION=c77c73a4bdeb6fb21fa7522239b2276e27ea10f8
ARG SAMTOOLS_VERSION=1.22.1

ENV PATH=/opt/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        python2 python2-dev git \
        libncurses6 zlib1g libbz2-1.0 liblzma5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/samtools /usr/local/bin/samtools

RUN mkdir -p /opt/bin \
    && git clone https://github.com/loganylchen/Aeron.git /tmp/Aeron \
    && cd /tmp/Aeron \
    && git checkout ${VERSION} \
    && cp Binaries/* /opt/bin/ \
    && cp AeronScripts/* /opt/bin/ \
    && chmod +x /opt/bin/* \
    && rm -rf /tmp/Aeron

RUN samtools --version | head -1

WORKDIR /data
CMD ["bash"]
