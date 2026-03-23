ARG VERSION=48df2c04ee063c96aaefde64df915a867528f93e
ARG HISAT2_VERSION=2.2.1
ARG SAMTOOLS_VERSION=1.21
ARG BEDTOOLS_VERSION=2.31.1
ARG MACS2_VERSION=2.2.9.1
ARG EXOMEPEAK2_VERSION=1.10.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ARG HISAT2_VERSION
ARG SAMTOOLS_VERSION
ARG BEDTOOLS_VERSION
ARG MACS2_VERSION
ARG EXOMEPEAK2_VERSION
ENV PATH=/opt/RNAMod:/usr/local/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        git \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        g++ \
        make \
        perl \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libncurses5-dev \
        libgomp1 \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        r-base \
        r-base-dev \
    # ── samtools ──────────────────────────────────────────────────────────────
    && wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
        -O /tmp/samtools.tar.bz2 \
    && tar -xjf /tmp/samtools.tar.bz2 -C /tmp \
    && cd /tmp/samtools-${SAMTOOLS_VERSION} \
    && ./configure --prefix=/usr/local && make -j$(nproc) && make install \
    # ── bedtools ──────────────────────────────────────────────────────────────
    && wget -q https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VERSION}/bedtools-${BEDTOOLS_VERSION}.tar.gz \
        -O /tmp/bedtools.tar.gz \
    && tar -xzf /tmp/bedtools.tar.gz -C /tmp \
    && cd /tmp/bedtools2 && make -j$(nproc) && cp bin/bedtools /usr/local/bin/ \
    # ── hisat2 ────────────────────────────────────────────────────────────────
    && wget -q https://github.com/DaehwanKimLab/hisat2/archive/refs/tags/v${HISAT2_VERSION}.tar.gz \
        -O /tmp/hisat2.tar.gz \
    && tar -xzf /tmp/hisat2.tar.gz -C /tmp \
    && cd /tmp/hisat2-${HISAT2_VERSION} && make -j$(nproc) \
    && cp hisat2 hisat2-align-s hisat2-align-l hisat2-build hisat2-build-s hisat2-build-l \
        hisat2-inspect hisat2-inspect-s hisat2-inspect-l \
        hisat2_extract_exons.py hisat2_extract_splice_sites.py /usr/local/bin/ \
    # ── macs2 ─────────────────────────────────────────────────────────────────
    && pip3 install --no-cache-dir --break-system-packages macs2==${MACS2_VERSION} \
    # ── R packages ────────────────────────────────────────────────────────────
    && Rscript -e " \
        install.packages('BiocManager', repos='https://cloud.r-project.org/'); \
        BiocManager::install('exomePeak2', ask=FALSE) \
    " \
    # ── RNAMod pipeline ───────────────────────────────────────────────────────
    && git clone --depth=50 https://github.com/Epigenomics-Lab/RNAMod.git /opt/RNAMod \
    && cd /opt/RNAMod && git checkout ${VERSION} \
    # ── cleanup ───────────────────────────────────────────────────────────────
    && apt-get purge -y --auto-remove wget ca-certificates git python3-dev gcc g++ make r-base-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN hisat2 --version | head -1

WORKDIR /data
CMD ["bash"]
