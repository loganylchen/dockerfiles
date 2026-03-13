ARG VERSION=3.1.1

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        pigz \
        lftp \
        curl \
    && wget -q https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/${VERSION}/sratoolkit.${VERSION}-ubuntu64.tar.gz \
        -O /tmp/sratoolkit.tar.gz \
    && tar -xzf /tmp/sratoolkit.tar.gz -C /opt \
    && mv /opt/sratoolkit.${VERSION}-ubuntu64 /opt/sratoolkit \
    && apt-get purge -y --auto-remove wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* /tmp/*

ENV PATH=/opt/sratoolkit/bin:$PATH

RUN fastq-dump --version

WORKDIR /data
CMD ["bash"]
