FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
ARG VERSION=1.0.1

ENV PATH=/opt/CPC2/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip wget g++ make \
    && pip3 install --no-cache-dir --break-system-packages biopython six \
    && cd /tmp \
    && wget -q https://github.com/gao-lab/CPC2_standalone/archive/refs/tags/v${VERSION}.tar.gz \
    && tar -zxf v${VERSION}.tar.gz \
    && cd CPC2_standalone-${VERSION}/libs/libsvm \
    && tar -zxf libsvm-3.18.tar.gz \
    && cd libsvm-3.18 \
    && make clean && make \
    && mv /tmp/CPC2_standalone-${VERSION} /opt/CPC2 \
    && chmod -R +x /opt/CPC2 \
    && apt-get purge -y --auto-remove wget g++ make \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN CPC2.py --help 2>&1 | head -3 || true

WORKDIR /data
CMD ["bash"]
