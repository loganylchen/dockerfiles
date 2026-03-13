ARG VERSION=4.3.0

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        gfortran \
        libgomp1 \
        samtools \
    && pip3 install --no-cache-dir --break-system-packages \
        rmats==${VERSION} \
    && apt-get purge -y --auto-remove python3-dev gcc gfortran \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN rmats.py --version

WORKDIR /data
CMD ["rmats.py"]
