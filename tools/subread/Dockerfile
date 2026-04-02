ARG VERSION=2.0.6

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        libgomp1 \
    && wget -q https://sourceforge.net/projects/subread/files/subread-${VERSION}/subread-${VERSION}-Linux-x86_64.tar.gz/download \
        -O /tmp/subread.tar.gz \
    && tar -xzf /tmp/subread.tar.gz -C /opt \
    && ln -s /opt/subread-${VERSION}-Linux-x86_64/bin/featureCounts /usr/local/bin/featureCounts \
    && ln -s /opt/subread-${VERSION}-Linux-x86_64/bin/subread-align /usr/local/bin/subread-align \
    && ln -s /opt/subread-${VERSION}-Linux-x86_64/bin/subread-buildindex /usr/local/bin/subread-buildindex \
    && ln -s /opt/subread-${VERSION}-Linux-x86_64/bin/exactSNP /usr/local/bin/exactSNP \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN featureCounts -v 2>&1

WORKDIR /data
CMD ["featureCounts"]
