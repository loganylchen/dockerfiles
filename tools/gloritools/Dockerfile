# Builder stage: compile bowtie and samtools; download STAR prebuilt binary
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG STAR_VERSION=2.7.11b
ARG BOWTIE_VERSION=1.3.1
ARG SAMTOOLS_VERSION=1.19

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget unzip zip xxd g++ make libncurses5-dev zlib1g-dev libbz2-dev liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

# STAR: use prebuilt static binary from release tarball
RUN cd /tmp \
    && wget -q https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz \
    && tar -xzf ${STAR_VERSION}.tar.gz \
    && cp STAR-${STAR_VERSION}/bin/Linux_x86_64/STAR /usr/local/bin/ \
    && strip /usr/local/bin/STAR

# Bowtie1
RUN cd /tmp \
    && wget -q https://altushost-swe.dl.sourceforge.net/project/bowtie-bio/bowtie/${BOWTIE_VERSION}/bowtie-${BOWTIE_VERSION}-src.zip \
    && unzip -q bowtie-${BOWTIE_VERSION}-src.zip \
    && cd bowtie-${BOWTIE_VERSION}-src \
    && make -j$(nproc) \
    && cp bowtie bowtie-build bowtie-inspect /usr/local/bin/ \
    && strip /usr/local/bin/bowtie*

# samtools
RUN cd /tmp \
    && wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && tar -jxf samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && cd samtools-${SAMTOOLS_VERSION} \
    && ./configure --prefix=/usr/local \
    && make -j$(nproc) && make install \
    && strip /usr/local/bin/samtools

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip git \
        libncurses6 zlib1g libbz2-1.0 liblzma5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/STAR /usr/local/bin/STAR
COPY --from=builder /usr/local/bin/bowtie /usr/local/bin/bowtie
COPY --from=builder /usr/local/bin/bowtie-build /usr/local/bin/bowtie-build
COPY --from=builder /usr/local/bin/bowtie-inspect /usr/local/bin/bowtie-inspect
COPY --from=builder /usr/local/bin/samtools /usr/local/bin/samtools

ADD requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir --break-system-packages -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt \
    && git clone --depth=1 https://github.com/liucongcas/GLORI-tools.git /opt/GLORI-tools

ENV PATH=/opt/GLORI-tools:/usr/local/bin:/usr/bin:/bin

RUN STAR --version && samtools --version | head -1

WORKDIR /data
CMD ["bash"]
