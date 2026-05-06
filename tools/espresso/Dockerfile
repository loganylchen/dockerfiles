ARG VERSION=1.6.0

FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# Build the bundled Parasail Perl XS module against the system perl.
# The build script clones jeffdaily/parasail v2.6.2 and compiles its C library
# with cmake, then builds Parasail.pm/Parasail.so against it.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        ca-certificates \
        unzip \
        perl \
        libperl-dev \
        libstorable-perl \
    && wget -q https://github.com/Xinglab/espresso/archive/refs/tags/v${VERSION}.tar.gz -O /tmp/espresso.tar.gz \
    && tar -xzf /tmp/espresso.tar.gz -C /opt \
    && mv /opt/espresso-${VERSION} /opt/espresso \
    && cd /opt/espresso/src/Parasail \
    && ./build \
    && rm -rf /opt/espresso/src/Parasail/parasail \
              /opt/espresso/src/Parasail/blib \
              /opt/espresso/src/Parasail/Makefile* \
              /tmp/*

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="ESPRESSO" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="ESPRESSO - Error Statistics PRomoted Evaluator of Splice Site Options for long-read RNA-seq" \
      org.opencontainers.image.source="https://github.com/Xinglab/espresso" \
      org.opencontainers.image.licenses="BSD-2-Clause"

# Runtime: perl (with threads + Storable), hmmer, blast+, samtools, minimap2.
# Visualization extras: python3 + numpy + UCSC tools (kept light).
RUN apt-get update && apt-get install -y --no-install-recommends \
        perl \
        libstorable-perl \
        hmmer \
        ncbi-blast+ \
        samtools \
        minimap2 \
        python3 \
        python3-numpy \
        zlib1g \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/espresso /opt/espresso

# The Parasail/build script installs Parasail.pm, Parasail.so and libparasail.so
# directly into /opt/espresso/src/ (one level up from Parasail/).
# ESPRESSO_*.pl uses `use lib dirname(__FILE__)` so they pick up Parasail.pm
# automatically; libparasail.so is loaded by DynaLoader at runtime, so it must
# be on LD_LIBRARY_PATH.
ENV PATH="/opt/espresso/src:$PATH" \
    LD_LIBRARY_PATH="/opt/espresso/src"

# Verify perl threading + Storable + ESPRESSO scripts + Parasail module load
RUN perl -e 'use threads; print("perl threads ok\n")' \
    && perl -e 'use Storable; die "old storable" if $Storable::VERSION < 3.0; print("Storable $Storable::VERSION ok\n")' \
    && perl -I/opt/espresso/src -e 'use Parasail; print("Parasail module ok\n")' \
    && perl /opt/espresso/src/ESPRESSO_S.pl --help 2>&1 | head -3 \
    && perl /opt/espresso/src/ESPRESSO_C.pl --help 2>&1 | head -3 \
    && perl /opt/espresso/src/ESPRESSO_Q.pl --help 2>&1 | head -3 \
    && hmmscan -h | head -1 \
    && blastn -version \
    && samtools --version | head -1 \
    && minimap2 --version

WORKDIR /data
CMD ["perl", "/opt/espresso/src/ESPRESSO_S.pl", "--help"]
