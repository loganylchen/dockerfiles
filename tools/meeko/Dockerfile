FROM python:3.11-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
ARG VERSION=0.7.1

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        libxrender1 \
        libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install meeko and dependencies (rdkit from pip)
RUN pip install --no-cache-dir \
    numpy scipy pandas \
    rdkit gemmi \
    meeko==${VERSION}

# Verify installation
RUN python -c "import meeko; print('meeko', meeko.__version__)"

WORKDIR /data
CMD ["python"]
