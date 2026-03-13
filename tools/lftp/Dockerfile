ARG VERSION=4.9.2

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        lftp \
        curl \
    && rm -rf /var/lib/apt/lists/*

RUN lftp --version | head -1

WORKDIR /data
CMD ["lftp"]
