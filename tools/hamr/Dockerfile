ARG VERSION=1.1.0

# Builder: compile samtools
FROM debian:bookworm-slim AS builder
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget ca-certificates g++ make libncurses-dev zlib1g-dev libbz2-dev liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && wget -q https://github.com/samtools/samtools/releases/download/1.18/samtools-1.18.tar.bz2 \
    && tar -jxf samtools-1.18.tar.bz2 \
    && cd samtools-1.18 \
    && ./configure --prefix=/usr/local \
    && make -j$(nproc) && make install \
    && strip /usr/local/bin/samtools

# Runtime stage
FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV PATH=/opt/bin:/opt/hamr:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip \
        r-base \
        git \
        libncurses6 zlib1g libbz2-1.0 liblzma5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/samtools /usr/local/bin/samtools

ADD https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static /opt/bin/bedtools

RUN pip3 install --no-cache-dir --break-system-packages rich \
    && git clone --depth=1 https://github.com/GregoryLab/HAMR.git /opt/hamr \
    && R -e 'install.packages("RColorBrewer", repos="https://cran.r-project.org")' \
    && chmod +x /opt/bin/bedtools /opt/hamr/* \
    && rm -rf /opt/hamr/.git

ADD hamr.py /opt/hamr/hamr.py

RUN samtools --version

WORKDIR /data
CMD ["bash"]
