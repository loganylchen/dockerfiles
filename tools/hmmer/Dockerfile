ARG VERSION=3.4

FROM debian:bookworm-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        build-essential \
    && wget -q http://eddylab.org/software/hmmer/hmmer-${VERSION}.tar.gz \
        -O /tmp/hmmer.tar.gz \
    && tar -xzf /tmp/hmmer.tar.gz -C /tmp \
    && cd /tmp/hmmer-${VERSION} \
    && ./configure --prefix=/opt/hmmer \
    && make -j$(nproc) \
    && make install \
    && strip /opt/hmmer/bin/* \
    && rm -rf /var/lib/apt/lists/* /tmp/*

FROM debian:bookworm-slim

COPY --from=builder /opt/hmmer /opt/hmmer

ENV PATH=/opt/hmmer/bin:$PATH

RUN /opt/hmmer/bin/hmmbuild -h | head -3

WORKDIR /data
CMD ["hmmbuild"]
