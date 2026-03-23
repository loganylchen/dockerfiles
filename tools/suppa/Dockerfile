ARG VERSION=2.3

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
    && pip3 install --no-cache-dir --break-system-packages \
        suppa==${VERSION} \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN suppa.py --help 2>&1 | head -3

WORKDIR /data
CMD ["suppa.py"]
