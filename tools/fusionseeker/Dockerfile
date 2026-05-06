ARG VERSION=1.0.1

FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

# Build bsalign (required by FusionSeeker for breakpoint polishing).
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        ca-certificates \
        zlib1g-dev \
    && git clone --depth 1 https://github.com/ruanjue/bsalign.git /tmp/bsalign \
    && cd /tmp/bsalign \
    && make \
    && install -m 0755 bsalign /usr/local/bin/bsalign

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="FusionSeeker" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="FusionSeeker - gene fusion caller for long-read transcriptome sequencing" \
      org.opencontainers.image.source="https://github.com/Maggi-Chen/FusionSeeker" \
      org.opencontainers.image.licenses="MIT"

# Pin to commit d33b11b (2023-08-02, post-v1.0.1 with "accept failed poa step"
# bugfix). Upstream has no release tag for it but the bundled script still
# self-reports v1.0.1.
ARG COMMIT=d33b11b

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pysam \
        minimap2 \
        samtools \
        wget \
        ca-certificates \
    && wget -q "https://github.com/Maggi-Chen/FusionSeeker/archive/${COMMIT}.tar.gz" -O /tmp/fs.tar.gz \
    && tar -xzf /tmp/fs.tar.gz -C /opt \
    && mv /opt/FusionSeeker-${COMMIT}* /opt/fusionseeker \
    && chmod +x /opt/fusionseeker/fusionseeker \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/* /tmp/*

COPY --from=builder /usr/local/bin/bsalign /usr/local/bin/bsalign

# fusionseeker entry script does `import construct_gtf` etc. (sibling modules)
# so we add the repo dir to PATH and PYTHONPATH.
ENV PATH="/opt/fusionseeker:$PATH" \
    PYTHONPATH="/opt/fusionseeker"

RUN python3 -c "import pysam" \
    && minimap2 --version \
    && samtools --version | head -1 \
    && bsalign 2>&1 | head -2 || true \
    && fusionseeker --version

WORKDIR /data
CMD ["fusionseeker", "-h"]
