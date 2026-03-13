FROM debian:bookworm-slim
ARG VERSION=1.84

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --break-system-packages \
        numpy \
        biopython==${VERSION}

RUN python3 -c "import Bio; print('biopython', Bio.__version__)"

WORKDIR /data
CMD ["python3"]
