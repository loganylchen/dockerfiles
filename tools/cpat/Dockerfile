ARG VERSION=3.0.4

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
    && pip3 install --no-cache-dir --break-system-packages \
        cpat==${VERSION} \
    && apt-get purge -y gcc \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN cpat.py --help 2>&1 || true

WORKDIR /data
CMD ["cpat.py"]
