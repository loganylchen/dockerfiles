ARG VERSION=2.1.0

# Optimized Dockerfile for ELIGOS2 v2.1.0
# Based on official Dockerfile: https://gitlab.com/piroonj/eligos2
# Uses conda/mamba for dependency management to ensure correct versions

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

# Install Miniconda
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm -f /tmp/miniconda.sh && \
    /opt/conda/bin/conda clean -afy && \
    rm -rf /root/.cache /tmp/*

ENV PATH="/opt/conda/bin:$PATH"

# Accept Conda Terms of Service
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# Create eligos2 conda environment with pinned versions (as recommended in GitLab README)
# bedtools=2.25 is critical - newer versions produce different BED output format
# pybedtools=0.8.0 is critical - ensures consistent BED column handling
RUN conda create -n eligos2 -c conda-forge -c bioconda -c r \
        python=3.6 \
        pysam=0.13 \
        pandas=0.23.4 \
        pybedtools=0.8.0 \
        bedtools=2.25 \
        rpy2=2.8.5 \
        r-base=3.4.1 \
        tqdm=4.40.2 \
        numpy=1.11.3 \
        -y && \
    conda clean -afy && \
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
