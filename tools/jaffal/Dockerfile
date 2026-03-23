ARG VERSION=2.3

# Builder: compile JAFFA tools and the local process_transcriptome_align_table.c++
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget g++ make git zlib1g-dev libbz2-dev liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

# Build seqtk (use wget instead of git clone to avoid network issues)
RUN wget -q https://github.com/lh3/seqtk/archive/refs/heads/master.tar.gz -O /tmp/seqtk.tar.gz \
    && tar -xzf /tmp/seqtk.tar.gz -C /tmp \
    && mv /tmp/seqtk-master /tmp/seqtk \
    && cd /tmp/seqtk && make -j$(nproc) && strip seqtk

# Download JAFFA and compile its tools
RUN cd /tmp \
    && wget -q https://github.com/Oshlack/JAFFA/releases/download/version-${VERSION}/JAFFA-version-${VERSION}.tar.gz \
    && tar -zxf JAFFA-version-${VERSION}.tar.gz \
    && g++ -O3 -o /tmp/extract_seq_from_fasta JAFFA-version-${VERSION}/src/extract_seq_from_fasta.c++ \
    && g++ -std=c++11 -O3 -o /tmp/make_simple_read_table JAFFA-version-${VERSION}/src/make_simple_read_table.c++ \
    && g++ -std=c++11 -O3 -o /tmp/make_3_gene_fusion_table JAFFA-version-${VERSION}/src/make_3_gene_fusion_table.c++ \
    && strip /tmp/extract_seq_from_fasta /tmp/make_simple_read_table /tmp/make_3_gene_fusion_table

# Compile the local custom tool
COPY process_transcriptome_align_table.c++ /tmp/
RUN g++ -std=c++11 -O3 -o /tmp/process_transcriptome_align_table /tmp/process_transcriptome_align_table.c++ \
    && strip /tmp/process_transcriptome_align_table

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION=2.3

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:/opt/softwares/JAFFA:$PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

RUN apt-get update && apt-get install -y --no-install-recommends \
        openjdk-17-jdk-headless \
        python3 \
        r-base \
        wget \
        zlib1g libbz2-1.0 liblzma5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /tmp/seqtk/seqtk /opt/bin/seqtk
COPY --from=builder /tmp/extract_seq_from_fasta /opt/bin/extract_seq_from_fasta
COPY --from=builder /tmp/make_simple_read_table /opt/bin/make_simple_read_table
COPY --from=builder /tmp/make_3_gene_fusion_table /opt/bin/make_3_gene_fusion_table
COPY --from=builder /tmp/process_transcriptome_align_table /opt/bin/process_transcriptome_align_table

RUN mkdir -p /opt/softwares \
    && wget -q https://github.com/Oshlack/JAFFA/releases/download/version-${VERSION}/JAFFA-version-${VERSION}.tar.gz -O /tmp/jaffa.tar.gz \
    && tar -zxf /tmp/jaffa.tar.gz -C /opt/softwares \
    && mv /opt/softwares/JAFFA-version-${VERSION} /opt/softwares/JAFFA \
    && rm /tmp/jaffa.tar.gz \
    && chmod +x /opt/bin/*

RUN seqtk 2>&1 | head -1 || true

WORKDIR /data
CMD ["bash"]
