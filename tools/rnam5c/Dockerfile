ARG VERSION=409be6485bcdd160f6c57e386ef71ff3ecb8e2f6
ARG HISAT2_VERSION=2.1.0
ARG BOWTIE_VERSION=2.3.5
ARG SAMTOOLS_VERSION=1.6

# python2 is not available on bookworm; use ubuntu:20.04 which still ships it
FROM ubuntu:20.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ARG HISAT2_VERSION
ARG BOWTIE_VERSION
ARG SAMTOOLS_VERSION
ENV PATH=/opt/RNA-m5C:/usr/local/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        python2 \
        python2-dev \
        python3 \
        python3-pip \
        python3-distutils \
        git \
        wget \
        ca-certificates \
        build-essential \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        libncurses5-dev \
        libgomp1 \
        unzip \
        bzip2 \
        curl \
    # ── pip2 via get-pip ──────────────────────────────────────────────────────
    && curl -sS https://bootstrap.pypa.io/pip/2.7/get-pip.py | python2 \
    && pip2 install --no-cache-dir \
        numpy==1.13.3 \
        scipy==0.19.1 \
        pysam==0.12.0.1 \
        biopython==1.70 \
    # ── samtools ──────────────────────────────────────────────────────────────
    && wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
        -O /tmp/samtools.tar.bz2 \
    && tar -xjf /tmp/samtools.tar.bz2 -C /tmp \
    && cd /tmp/samtools-${SAMTOOLS_VERSION} \
    && ./configure --prefix=/usr/local && make -j$(nproc) && make install \
    # ── hisat2 ────────────────────────────────────────────────────────────────
    && wget -q https://cloud.biohpc.swmed.edu/index.php/s/hisat2-210-Linux_x86_64/download \
        -O /tmp/hisat2.zip \
    && unzip -q /tmp/hisat2.zip -d /opt \
    && mv /opt/hisat2-${HISAT2_VERSION} /opt/hisat2 \
    && ln -sf /opt/hisat2/hisat2* /usr/local/bin/ \
    && ln -sf /opt/hisat2/*.py /usr/local/bin/ \
    # ── bowtie2 ───────────────────────────────────────────────────────────────
    && wget -q https://github.com/BenLangmead/bowtie2/releases/download/v${BOWTIE_VERSION}/bowtie2-${BOWTIE_VERSION}-linux-x86_64.zip \
        -O /tmp/bowtie2.zip \
    && unzip -q /tmp/bowtie2.zip -d /opt \
    && mv /opt/bowtie2-${BOWTIE_VERSION}-linux-x86_64 /opt/bowtie2 \
    && ln -sf /opt/bowtie2/bowtie2* /usr/local/bin/ \
    # ── RNA-m5C pipeline ──────────────────────────────────────────────────────
    && git clone --depth=50 https://github.com/loganylchen/RNA-m5C.git /opt/RNA-m5C \
    && cd /opt/RNA-m5C && git checkout ${VERSION} \
    # ── cleanup ───────────────────────────────────────────────────────────────
    && apt-get purge -y --auto-remove build-essential wget git curl \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN hisat2 --version

WORKDIR /data
CMD ["bash"]
