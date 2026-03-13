FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH

ADD https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static /opt/bin/bedtools

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip git \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x /opt/bin/bedtools

RUN pip3 install --no-cache-dir --break-system-packages \
        git+https://github.com/loganylchen/LAFITE.git

RUN LAFITE --help 2>&1 | head -1

WORKDIR /data
CMD ["LAFITE"]
