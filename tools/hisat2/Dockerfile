ARG VERSION=2.2.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        build-essential \
        python3 \
        libgomp1 \
    && wget -q https://github.com/DaehwanKimLab/hisat2/archive/refs/tags/v${VERSION}.tar.gz \
        -O /tmp/hisat2.tar.gz \
    && tar -xzf /tmp/hisat2.tar.gz -C /tmp \
    && cd /tmp/hisat2-${VERSION} \
    && make -j$(nproc) \
    && cp hisat2 hisat2-align-s hisat2-align-l hisat2-build hisat2-build-s hisat2-build-l \
        hisat2-inspect hisat2-inspect-s hisat2-inspect-l \
        hisat2_extract_exons.py hisat2_extract_snps_haplotypes_UCSC.py \
        hisat2_extract_snps_haplotypes_VCF.py hisat2_extract_splice_sites.py \
        hisat2_read_statistics.py hisat2_simulate_reads.py \
        /usr/local/bin/ \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN hisat2 --version

WORKDIR /data
CMD ["hisat2"]
