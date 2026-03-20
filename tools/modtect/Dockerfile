ARG VERSION=1.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

ENV PATH=/opt/bin:/opt/modtect:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        samtools git python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth=1 https://github.com/ktan8/ModTect.git /opt/modtect

ADD modtect.py /opt/modtect/modtect.py

RUN chmod +x /opt/modtect/* \
    && samtools --version | head -1

WORKDIR /data
CMD ["bash"]
