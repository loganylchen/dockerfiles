ARG VERSION=4.6.1.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        openjdk-17-jre-headless \
        python3 \
        python3-pip \
        r-base \
    && wget -q https://github.com/broadinstitute/gatk/releases/download/${VERSION}/gatk-${VERSION}.zip \
        -O /tmp/gatk.zip \
    && unzip /tmp/gatk.zip -d /opt \
    && mv /opt/gatk-${VERSION} /opt/gatk \
    && apt-get purge -y --auto-remove wget ca-certificates unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/*

ENV PATH=/opt/gatk:$PATH

RUN gatk --version

WORKDIR /data
CMD ["gatk"]
