ARG VERSION=2.4.42

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
    && wget -q https://github.com/bedops/bedops/releases/download/v${VERSION}/bedops_linux_x86_64-v${VERSION}.tar.bz2 \
        -O /tmp/bedops.tar.bz2 \
    && tar -xjf /tmp/bedops.tar.bz2 -C /tmp \
    && cp /tmp/bin/* /usr/local/bin/ \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN bedops --version

WORKDIR /data
CMD ["bedops"]
