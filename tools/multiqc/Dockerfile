ARG VERSION=1.24.1

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
    && pip3 install --no-cache-dir --break-system-packages \
        multiqc==${VERSION} \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN multiqc --version

WORKDIR /data
CMD ["multiqc"]
