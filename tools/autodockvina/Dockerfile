ARG VERSION=1.2.5

FROM python:3.10-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH=/opt/bin:/opt/mgltools/bin:/opt/adfr/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        build-essential \
        gzip \
        libboost-all-dev \
        swig \
        git \
        ffmpeg \
        libsm6 \
        libxext6 \
    # ── MGLTools ──────────────────────────────────────────────────────────────
    && cd /tmp \
    && wget -q https://ccsb.scripps.edu/download/532/ -O mgltools.tar.gz \
    && tar -xzf mgltools.tar.gz \
    && cd mgltools_x86_64Linux2_1.5.7 \
    && ./install.sh -d /opt/mgltools \
    # ── AutoDock-Vina (pre-built binaries) ────────────────────────────────────
    && mkdir -p /opt/bin \
    && wget -q https://github.com/ccsb-scripps/AutoDock-Vina/releases/download/v${VERSION}/vina_${VERSION}_linux_x86_64 \
        -O /opt/bin/vina \
    && wget -q https://github.com/ccsb-scripps/AutoDock-Vina/releases/download/v${VERSION}/vina_split_${VERSION}_linux_x86_64 \
        -O /opt/bin/vina_split \
    && chmod +x /opt/bin/vina /opt/bin/vina_split \
    # Clone source for Python bindings and scripts
    && git clone --depth=1 --branch v${VERSION} https://github.com/ccsb-scripps/AutoDock-Vina /tmp/AutoDock-Vina \
    # ── ADFRsuite ─────────────────────────────────────────────────────────────
    && cd /tmp \
    && wget -q https://ccsb.scripps.edu/adfr/download/1028/ -O ADFT_install \
    && chmod +x ADFT_install \
    && ./ADFT_install --prefix /tmp/adfr --mode silent \
    && cd /tmp/adfr \
    && tar -xzf ADFRsuite_x86_64Linux_1.0.tar.gz \
    && cd ADFRsuite_x86_64Linux_1.0 \
    && ./install.sh -d /opt/adfr -c 0 -l \
    # ── Vina Python bindings + scripts ────────────────────────────────────────
    && cd /tmp/AutoDock-Vina/build/python \
    && python3 setup.py build install \
    && cd /tmp/AutoDock-Vina/example/autodock_scripts \
    && 2to3 -w . \
    && cp *.py /opt/bin/ \
    && chmod +x /opt/bin/* \
    # ── AutoDock4 binary ──────────────────────────────────────────────────────
    && cd /tmp \
    && wget -q https://autodock.scripps.edu/wp-content/uploads/sites/56/2021/10/autodocksuite-4.2.6-x86_64Linux2.tar \
        -O autodocksuite.tar \
    && tar -xf autodocksuite.tar \
    && cp x86_64Linux2/* /opt/bin/ \
    # ── cleanup ───────────────────────────────────────────────────────────────
    && apt-get purge -y --auto-remove build-essential swig git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN vina --version

WORKDIR /data
CMD ["python3"]
