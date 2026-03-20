ARG VERSION=2.1.0

# Optimized Dockerfile for ELIGOS2 v2.1.0
# Based on official README: https://gitlab.com/piroonj/eligos2
# Uses mamba for faster dependency resolution

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

# Install minimal system dependencies for conda
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        git \
        gawk \
        && rm -rf /var/lib/apt/lists/*

# Install Miniforge (includes mamba, avoids Anaconda TOS issues)
RUN wget -q https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh \
    -O /tmp/miniforge.sh && \
    bash /tmp/miniforge.sh -b -p /opt/conda && \
    rm -f /tmp/miniforge.sh && \
    /opt/conda/bin/conda clean -afy && \
    rm -rf /root/.cache /tmp/*

ENV PATH="/opt/conda/bin:$PATH"

# Create eligos2 conda environment using mamba (as recommended in official README)
# Using Python 3.10 with unpinned versions to avoid dependency conflicts
RUN mamba create -n eligos2 -c conda-forge -c bioconda -c r \
        python=3.10 \
        pysam \
        pandas \
        pybedtools \
        bedtools \
        rpy2 \
        r-base \
        tqdm \
        numpy \
        -y && \
    mamba clean -afy && \
    rm -rf /tmp/*

# Install R package samplesizeCMH in the conda R environment
RUN conda run -n eligos2 Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")'

# Clone ELIGOS2
RUN git clone --depth=1 --branch v${VERSION} https://gitlab.com/piroonj/eligos2.git /opt/eligos2 && \
    chmod +x /opt/eligos2/*.py /opt/eligos2/Scripts/* 2>/dev/null || true

# Create wrapper script for running eligos2 in conda environment
RUN printf '#!/bin/bash\n\
source /opt/conda/etc/profile.d/conda.sh\n\
conda activate eligos2\n\
python /opt/eligos2/eligos2.py "$@"\n' > /usr/local/bin/eligos2 && \
    chmod +x /usr/local/bin/eligos2

# Verify installations
RUN conda run -n eligos2 bedtools --version && \
    conda run -n eligos2 python -c "import pybedtools; print(f'pybedtools {pybedtools.__version__}')" && \
    eligos2 -h

WORKDIR /data

CMD ["eligos2", "-h"]
