# Multi-stage build for EpiNano - optimized for size
# EpiNano requires Python 3.6-3.7 and R for some analysis scripts
# Stage 1: Builder - Install dependencies and download EpiNano
FROM python:3.7-slim AS builder

ARG VERSION=1.2.5

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download and extract EpiNano
RUN git clone https://github.com/novoalab/EpiNano.git && \
    cd EpiNano && \
    git checkout EpiNano${VERSION} && \
    rm -rf .git && \
    cd .. && \
    mv EpiNano /opt/epinano 

# Create virtual environment and install Python dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install Python dependencies for EpiNano
# Using compatible versions for Python 3.7
RUN pip install --no-cache-dir \
    numpy==1.19.5 \
    pandas==1.1.5 \
    scipy==1.5.4 \
    scikit-learn==0.23.2 \
    biopython==1.78 \
    pysam==0.16.0.1 \
    h5py==2.10.0

# Stage 2: Runtime - Minimal image with only runtime dependencies
FROM python:3.7-slim

ARG VERSION=1.2.5

LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="EpiNano - Detection of RNA modifications from Oxford Nanopore direct RNA sequencing"
LABEL version="${VERSION}"

# Install runtime dependencies
# samtools for BAM processing, openjdk-17-jre-headless for sam2tsv.jar, R for analysis scripts
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    samtools \
    openjdk-17-jre-headless \
    r-base \
    r-cran-ggplot2 \
    r-cran-optparse \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install R packages required for EpiNano
RUN Rscript -e "install.packages(c('outliers', 'reshape2', 'car', 'ggrepel'), repos='https://cloud.r-project.org/', dependencies=TRUE)"

# Copy EpiNano from builder
COPY --from=builder /opt/epinano /opt/epinano

# Copy Python virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set PATH to include virtual environment and EpiNano scripts
ENV PATH="/opt/venv/bin:/opt/epinano:$PATH"
ENV SAM2TSV="/opt/epinano/misc/sam2tsv.jar"

# Make Python scripts executable
RUN chmod +x /opt/epinano/*.py /opt/epinano/*.sh

# Set working directory
WORKDIR /data

# Verify installation
RUN python --version && \
    python -c "import numpy, pandas, scipy, sklearn, Bio, pysam, h5py; print('Python dependencies installed successfully')" && \
    samtools --version | head -1 && \
    java -version 2>&1 | head -1 && \
    Rscript --version 2>&1 | head -1 && \
    ls -la /opt/epinano/*.py | head -5

# Default command - show help
CMD ["python", "/opt/epinano/Epinano_Variants.py", "-h"]
