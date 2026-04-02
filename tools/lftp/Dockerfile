ARG VERSION=4.9.2

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        lftp \
        curl \
    && rm -rf /var/lib/apt/lists/*

RUN lftp --version

WORKDIR /data
CMD ["lftp"]
