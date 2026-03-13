FROM debian:bookworm-slim
ARG VERSION=1.1.2

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --break-system-packages \
        scaden==${VERSION}

RUN scaden --help 2>&1 | head -1

WORKDIR /data
CMD ["scaden"]
