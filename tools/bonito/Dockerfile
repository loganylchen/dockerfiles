ARG CUDA_VERSION
ARG VERSION
FROM nvidia/cuda:$CUDA_VERSION-cudnn-devel-ubuntu22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install ont-bonito==${VERSION} 

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*
