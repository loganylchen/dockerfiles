ARG VERSION=1.11.4

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        libgomp1 \
        libtbb12 \
    && MINOR=$(echo ${VERSION} | cut -d. -f2) \
    && if [ "$MINOR" -le 10 ]; then \
        wget -q https://github.com/COMBINE-lab/salmon/releases/download/v${VERSION}/salmon-${VERSION}_linux_x86_64.tar.gz \
            -O /tmp/salmon.tar.gz; \
    else \
        wget -q https://github.com/COMBINE-lab/salmon/releases/download/v${VERSION}/salmon-linux-x86_64.tar.gz \
            -O /tmp/salmon.tar.gz; \
    fi \
    && tar -xzf /tmp/salmon.tar.gz -C /opt \
    && cp $(find /opt -name "salmon" -type f -path "*/bin/salmon") /usr/local/bin/salmon \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/* /opt/salmon*

RUN salmon --version

WORKDIR /data
CMD ["salmon"]
