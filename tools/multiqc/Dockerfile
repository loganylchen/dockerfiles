ARG VERSION=1.24.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="MultiQC" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="MultiQC - aggregate results from bioinformatics analyses into a single report" \
      org.opencontainers.image.source="https://multiqc.info" \
      org.opencontainers.image.licenses="GPL-3.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
    && pip3 install --no-cache-dir --break-system-packages \
        multiqc==${VERSION} \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN multiqc --version

WORKDIR /data
CMD ["multiqc"]
