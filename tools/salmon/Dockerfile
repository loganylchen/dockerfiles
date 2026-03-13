ARG VERSION=1.10.3

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        libgomp1 \
    && wget -q https://github.com/COMBINE-lab/salmon/releases/download/v${VERSION}/salmon-${VERSION}_linux_x86_64.tar.gz \
        -O /tmp/salmon.tar.gz \
    && tar -xzf /tmp/salmon.tar.gz -C /opt \
    && ln -s /opt/salmon-${VERSION}_linux_x86_64/bin/salmon /usr/local/bin/salmon \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN salmon --version

WORKDIR /data
CMD ["salmon"]
