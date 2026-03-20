ARG VERSION=1.0.2

FROM python:3.11-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH

# Install system dependencies and bedtools
RUN apt-get update && apt-get install -y --no-install-recommends \
        bedtools \
    && rm -rf /var/lib/apt/lists/*

# Install LAFITE and dependencies
RUN pip install --no-cache-dir LAFITE==${VERSION}

# Verify installation
RUN lafite --help 2>&1 | head -3

WORKDIR /data
CMD ["lafite"]
