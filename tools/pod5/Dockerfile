ARG VERSION=0.3.39

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="pod5" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="Oxford Nanopore POD5 file format Python API and CLI tools (inspect, convert, subset, merge, repack)" \
      org.opencontainers.image.source="https://github.com/nanoporetech/pod5-file-format" \
      org.opencontainers.image.licenses="MPL-2.0"

# pod5 is a pure-Python package (wheels for lib-pod5, pyarrow, polars, h5py),
# so no compiler toolchain is needed at install time.
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python-is-python3 \
    && pip3 install --no-cache-dir --break-system-packages \
        "pod5==${VERSION}" \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

# Smoke test
RUN pod5 --version \
    && python -c "import pod5; print('pod5', pod5.__version__)"

WORKDIR /data
CMD ["pod5"]
