ARG VERSION=0.24.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH="/opt/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
    && mkdir -p /opt/bin/ \
    && wget http://opengene.org/fastp/fastp.${VERSION} -o /opt/bin/fastp \
    && chmod a+x /opt/bin/fastp \
    && rm -rf /var/lib/apt/lists/*


RUN fastp --version 2>&1

WORKDIR /data
CMD ["fastp"]
