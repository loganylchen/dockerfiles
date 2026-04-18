ARG VERSION=2.3

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="SUPPA" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="SUPPA2 - fast, accurate, and uncertainty-aware differential splicing analysis" \
      org.opencontainers.image.source="https://github.com/comprna/SUPPA" \
      org.opencontainers.image.licenses="MIT"

ENV PATH="/opt/suppa:${PATH}"
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget unzip python3 python3-pip python3-dev ca-certificates \
    && pip3 install --no-cache-dir --break-system-packages \
        SUPPA==${VERSION} \
    && wget -q https://github.com/comprna/SUPPA/archive/refs/tags/v${VERSION}.zip \
    && unzip v${VERSION}.zip \
    && mv SUPPA-${VERSION} /opt/suppa \
    && chmod -R +x /opt/suppa \
    && ln -s /opt/suppa/suppa.py /usr/local/bin/suppa.py \
    && apt-get purge -y --auto-remove wget unzip python3-dev ca-certificates \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/* v${VERSION}.zip

RUN python3 /opt/suppa/suppa.py --help 2>&1

WORKDIR /data
CMD ["python3", "/opt/suppa/suppa.py"]
