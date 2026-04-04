ARG VERSION=1.1.2

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip gcc libhdf5-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --break-system-packages \
        scaden==${VERSION}

RUN scaden --help 2>&1

WORKDIR /data
CMD ["scaden"]
