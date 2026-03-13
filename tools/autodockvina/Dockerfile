ARG VERSION=1.2.5

FROM python:3.10-slim

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
    # ── AutoDock-Vina ─────────────────────────────────────────────────────────
    && cd /tmp \
    && mkdir -p /opt/bin \
    && git clone --depth=1 --branch v${VERSION} https://github.com/ccsb-scripps/AutoDock-Vina /tmp/AutoDock-Vina \
    && cd /tmp/AutoDock-Vina/build/linux/release \
    && make \
    && strip vina vina_split \
    && cp vina vina_split /opt/bin/ \
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
