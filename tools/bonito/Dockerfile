FROM nvidia/cuda:12.8.1-base-ubuntu22.04
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install flash-attn --no-build-isolation && \
    pip install --upgrade pip && \
    pip install ont-bonito==${VERSION} 

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*
