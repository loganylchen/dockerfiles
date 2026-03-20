ARG VERSION=1.0
ARG DORADO_VERSION=0.6.2

FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"
LABEL description="DirectRM - RNA modification detection from Nanopore dRNA-Seq data"

ENV DEBIAN_FRONTEND=noninteractive


# Install base dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    git \
    bzip2 \
    libhdf5-103 \
    libbz2-1.0 \
    liblzma5 \
    libgomp1 \
    samtools \
    && rm -rf /var/lib/apt/lists/* /tmp/*

# Install Miniconda
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    -O /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p /opt/conda \
    && rm -f /tmp/miniconda.sh \
    && /opt/conda/bin/conda clean -afy \
    && rm -rf /root/.cache /tmp/*

ENV PATH="/opt/conda/bin:$PATH"

# Accept Conda Terms of Service
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# Create DirectRM conda environment (Python 3.11, PyTorch 2.1.2+cu118, CUDA 11.8)
RUN conda create -n directrm python=3.11 -y \
    && conda run -n directrm \
    pip install --no-cache-dir torch==2.1.2+cu118 --index-url https://download.pytorch.org/whl/cu118 \
    && conda run -n directrm \
    pip install --no-cache-dir \
    faiss-cpu \
    transformers==4.38.2 \
    numpy==1.26.2 \
    pandas==2.1.4 \
    scipy==1.13.0 \
    scikit-learn==1.4.2 \
    xgboost==2.1.3 \
    einops==0.7.0 \
    statsmodels==0.14.1 \
    biopython \
    pysam \
    tqdm \
    matplotlib \
    pyyaml \
    upsetplot \
    ont-pod5 \
    && conda clean -afy \
    && rm -rf /tmp/*

# Clone and install DirectRM
# VERSION can be: tag (v1.0), branch name, or commit hash
RUN git clone --depth 1 --branch v${VERSION} https://github.com/yuxinPenny/DirectRM.git /tmp/DirectRM \
    && cp -r /tmp/DirectRM /opt/DirectRM \
    && rm -rf /tmp/DirectRM /tmp/*

# Create Remora conda environment (Python 3.9, PyTorch 2.3.0+cu118, CUDA 11.8 compatible)
RUN conda create -n remora python=3.9 -y \
    && conda run -n remora \
    pip install --no-cache-dir torch==2.3.0 --index-url https://download.pytorch.org/whl/cu118 \
    && conda run -n remora \
    pip install --no-cache-dir \
    remora \
    ont-pod5 \
    tqdm \
    numpy \
    pandas \
    pytoml \
    && rm -rf /tmp/*

# Install Dorado binary
RUN wget -q https://github.com/nanoporetech/dorado/releases/download/v${DORADO_VERSION}/dorado-${DORADO_VERSION}-linux-x64.tar.gz \
    -O /tmp/dorado.tar.gz \
    && tar -xzf /tmp/dorado.tar.gz -C /tmp \
    && mkdir -p /opt/dorado \
    && cp -r /tmp/dorado-${DORADO_VERSION}-linux-x64/* /opt/dorado/ \
    && rm -rf /tmp/dorado.tar.gz /tmp/dorado-${DORADO_VERSION}-linux-x64 /tmp/*

ENV PATH="/opt/dorado/bin:$PATH"
ENV DIRECTRM_DIR="/opt/DirectRM"

# Create wrapper scripts for conda environments
# directrm_run: Run Python scripts in DirectRM environment
RUN printf '#!/bin/bash\n\
    source /opt/conda/etc/profile.d/conda.sh\n\
    conda activate directrm\n\
    python "$@"\n' > /usr/local/bin/directrm_run && \
    chmod +x /usr/local/bin/directrm_run

# remora_run: Run Remora in its isolated environment
RUN printf '#!/bin/bash\n\
    source /opt/conda/etc/profile.d/conda.sh\n\
    conda activate remora\n\
    remora "$@"\n' > /usr/local/bin/remora_run && \
    chmod +x /usr/local/bin/remora_run

# Verify installations
RUN dorado --version \
    && samtools --version | head -1 \
    && conda run -n directrm python -c "import torch; print(f'DirectRM env: PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}')" \
    && conda run -n remora python -c "import torch; print(f'Remora env: PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}')"

WORKDIR /data

# Copy the pipeline script from local directory
COPY directrm_pipeline.sh /opt/directrm_pipeline.sh
RUN chmod +x /opt/directrm_pipeline.sh

CMD ["bash"]
