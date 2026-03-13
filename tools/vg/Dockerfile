ARG VERSION=1.59.0

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
    && wget -q https://github.com/vgteam/vg/releases/download/v${VERSION}/vg \
        -O /usr/local/bin/vg \
    && chmod +x /usr/local/bin/vg \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN vg version

WORKDIR /data
CMD ["vg"]
