ARG VERSION=1.1.2

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install CPU-only torch first to keep image small, then scTAPE
RUN pip3 install --no-cache-dir --break-system-packages \
        torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip3 install --no-cache-dir --break-system-packages \
        scTAPE==${VERSION}

RUN python3 -c "import TAPE; print('scTAPE OK')"

WORKDIR /data
CMD ["python3"]
