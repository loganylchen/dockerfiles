ARG VERSION=0.9.4

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="oarfish" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="oarfish - transcript-level quantification from long-read RNA-seq" \
      org.opencontainers.image.source="https://github.com/COMBINE-lab/oarfish" \
      org.opencontainers.image.licenses="BSD-3-Clause"

# Prebuilt static-ish binary from upstream release. Only needs libgcc/libc at
# runtime; no extra deps required.
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        xz-utils \
    && wget -q "https://github.com/COMBINE-lab/oarfish/releases/download/v${VERSION}/oarfish-x86_64-unknown-linux-gnu.tar.xz" -O /tmp/oarfish.tar.xz \
    && tar -xJf /tmp/oarfish.tar.xz -C /tmp \
    && mv /tmp/oarfish-x86_64-unknown-linux-gnu/oarfish /usr/local/bin/oarfish \
    && chmod +x /usr/local/bin/oarfish \
    && strip /usr/local/bin/oarfish || true \
    && apt-get purge -y --auto-remove wget xz-utils \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN oarfish --version

WORKDIR /data
CMD ["oarfish", "--help"]
