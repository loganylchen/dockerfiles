ARG VERSION=1.5.7

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH=/opt/mgltools/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        build-essential \
        gzip \
    && cd /tmp \
    && wget -q https://ccsb.scripps.edu/download/532/ -O mgltools.tar.gz \
    && tar -xzf mgltools.tar.gz \
    && cd mgltools_x86_64Linux2_1.5.7 \
    && ./install.sh -d /opt/mgltools \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN /opt/mgltools/bin/python -c "import MolKit; print('MGLTools ok')"

WORKDIR /data
CMD ["/opt/mgltools/bin/python"]
