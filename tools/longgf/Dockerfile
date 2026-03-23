ARG VERSION=0.1.2

# Builder stage: compile LongGF against htslib
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget g++ make zlib1g-dev libbz2-dev liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

# Build htslib
RUN cd /tmp \
    && wget -q https://github.com/samtools/htslib/releases/download/1.19/htslib-1.19.tar.bz2 \
    && tar -jxf htslib-1.19.tar.bz2 \
    && cd htslib-1.19 \
    && ./configure --prefix=/opt/htslib --disable-libcurl \
    && make -j$(nproc) && make install

# Build LongGF
RUN cd /tmp \
    && wget -q https://github.com/WGLab/LongGF/archive/refs/tags/v${VERSION}.tar.gz \
    && tar -xzf v${VERSION}.tar.gz \
    && cd LongGF-${VERSION}/bin \
    && g++ -g -Wall -O3 -std=c++11 \
        -I/opt/htslib/include \
        -L/opt/htslib/lib \
        -o LongGF _com_fun_.c _gtf_struct_.c get_gfFrombam.c \
        /opt/htslib/lib/libhts.a -lz -lbz2 -llzma \
    && strip LongGF

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /tmp/LongGF-*/bin/LongGF /usr/local/bin/LongGF

RUN LongGF 2>&1 | head -3 || true

WORKDIR /data
CMD ["LongGF"]
