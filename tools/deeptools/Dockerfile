ARG VERSION=3.5.4

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-dev \
        gcc \
        locales \
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen \
    && pip3 install --no-cache-dir --break-system-packages \
        deeptools==${VERSION} \
    && apt-get purge -y --auto-remove python3-dev gcc \
    && rm -rf /var/lib/apt/lists/* /root/.cache

RUN deeptools --version

WORKDIR /data
CMD ["bash"]
