# Build stage
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION=2.1.0
ARG SAMTOOLSVER=1.19.2

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libncurses-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        git && \
    rm -rf /var/lib/apt/lists/*

# Build samtools from source
WORKDIR /tmp
RUN curl -L https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 | tar -jxf - && \
    cd samtools-${SAMTOOLSVER} && \
    ./configure --without-curses && \
    make && \
    strip samtools

# Clone eligos2 at the specified version tag
RUN git clone --depth=1 --branch v${VERSION} https://gitlab.com/piroonj/eligos2.git /opt/eligos2 && \
    chmod +x /opt/eligos2/*.py /opt/eligos2/Scripts/* 2>/dev/null || true

# Patch eligos2 to remove deprecated pandas2ri.activate() calls
RUN sed -i 's/^pandas2ri.activate()/#pandas2ri.activate()  # Commented out due to rpy2 deprecation/' /opt/eligos2/_pair_diff_mod.py && \
    sed -i 's/^pandas2ri.activate()/#pandas2ri.activate()  # Commented out due to rpy2 deprecation/' /opt/eligos2/_rna_mod.py && \
    sed -i 's/^pandas2ri.activate()/#pandas2ri.activate()  # Commented out due to rpy2 deprecation/' /opt/eligos2/_multi_samples_test.py && \
    sed -i 's/^\s*pandas2ri\.activate()/#pandas2ri.activate()  # Commented out due to rpy2 deprecation/' /opt/eligos2/_eligos_func.py

# Patch eligos2 to fix bedtools merge output (ensure strand column is preserved)
# Original: merge(s=True,c='4',o='distinct') outputs only 4 columns
# Fixed: merge with explicit column handling to ensure 5 columns (chrom,start,end,strand,name)
RUN sed -i "s/mergedBed = beds.sort().merge(s=True,c='4',o='distinct')/mergedBed = beds.sort().merge(s=True, c='4,5,6', o='distinct,distinct,distinct')/" /opt/eligos2/_misc.py && \
    sed -i 's/name = row\[4\]/name = row[5] if len(row) > 5 else row[4]/' /opt/eligos2/_eligos_func.py

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION=2.1.0
ARG SAMTOOLSVER=1.19.2

# Install build tools + runtime deps, compile Python packages (rpy2/pysam need
# make + r-base-dev + gcc), install R package, then purge build tools —
# all in one layer so build artifacts never persist in the image.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        make \
        r-base \
        r-base-dev \
        bedtools \
        gawk \
        zlib1g \
        libbz2-1.0 \
        liblzma5 \
        libcurl3-gnutls \
        libssl3 \
        ca-certificates \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    pip3 install --no-cache-dir --break-system-packages \
        pysam \
        pandas \
        pybedtools \
        rpy2 \
        tqdm \
        numpy && \
    Rscript -e 'install.packages("samplesizeCMH", repos="https://cloud.r-project.org")' && \
    apt-get purge -y --auto-remove \
        python3-dev \
        gcc \
        make \
        r-base-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/downloaded_packages /root/.R

# Copy samtools binary from builder
COPY --from=builder /tmp/samtools-${SAMTOOLSVER}/samtools /usr/local/bin/samtools

# Copy eligos2 from builder
COPY --from=builder /opt/eligos2 /opt/eligos2

# Add eligos2 to PATH and create python symlink
RUN ln -sf /usr/bin/python3 /usr/local/bin/python

ENV PATH="/opt/eligos2:/opt/eligos2/Scripts:${PATH}"

# Smoke-test
RUN samtools --version | head -1 && \
    eligos2 -h

WORKDIR /data

CMD ["eligos2", "-h"]
