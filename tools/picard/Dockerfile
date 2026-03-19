ARG VERSION=3.2.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        openjdk-17-jre-headless \
    && wget -q https://github.com/broadinstitute/picard/releases/download/${VERSION}/picard.jar \
        -O /opt/picard.jar \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN echo '#!/bin/sh\nexec java -jar /opt/picard.jar "$@"' > /usr/local/bin/picard \
    && chmod +x /usr/local/bin/picard

RUN picard SortSam --version 2>&1 | head -1

WORKDIR /data
CMD ["picard"]
