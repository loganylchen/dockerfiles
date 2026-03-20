ARG VERSION=2.1.0

# Optimized Dockerfile for ELIGOS2 v2.1.0
# Based on official Dockerfile: https://gitlab.com/piroonj/eligos2

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        g++ \
        make \
        git \
        r-base \
        r-base-dev \
        bedtools \
        gawk \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        libreadline-dev \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
# Using rpy2<3.5.0 to avoid pandas2ri.activate() deprecation warning
RUN pip3 install --no-cache-dir --break-system-packages \
    pysam \
    pandas \
    pybedtools \
    "rpy2<3.5.0" \
    tqdm \
    numpy

# Install R package
RUN Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")'

# Clone ELIGOS2
RUN git clone --depth=1 --branch v${VERSION} https://gitlab.com/piroonj/eligos2.git /opt/eligos2 && \
    chmod +x /opt/eligos2/*.py /opt/eligos2/Scripts/* 2>/dev/null || true

# Add python symlink (Debian 12 only has python3, but eligos2 uses #!/usr/bin/env python)
RUN ln -sf /usr/bin/python3 /usr/local/bin/python

# Add eligos2 to PATH
ENV PATH="/opt/eligos2:/opt/eligos2/Scripts:${PATH}"

# Smoke-test
RUN eligos2 -h

WORKDIR /data

CMD ["eligos2", "-h"]
