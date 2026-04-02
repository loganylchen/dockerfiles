ARG VERSION=c77c73a4bdeb6fb21fa7522239b2276e27ea10f8

FROM ubuntu:20.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

ENV PATH=/opt/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        python2 python2-dev git \
        samtools \
        ca-certificates \
        libncurses6 zlib1g libbz2-1.0 liblzma5 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/bin \
    && git clone https://github.com/loganylchen/Aeron.git /tmp/Aeron \
    && cd /tmp/Aeron \
    && git checkout ${VERSION} \
    && cp Binaries/* /opt/bin/ \
    && cp AeronScripts/* /opt/bin/ \
    && chmod +x /opt/bin/* \
    && rm -rf /tmp/Aeron

RUN samtools --version

WORKDIR /data
CMD ["bash"]
