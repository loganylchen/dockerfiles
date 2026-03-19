ARG VERSION=2.7.11b

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        unzip \
    && wget -q https://github.com/alexdobin/STAR/releases/download/${VERSION}/STAR_${VERSION}.zip \
    && unzip -p STAR_${VERSION}.zip "STAR_${VERSION}/Linux_x86_64_static/STAR" > /usr/local/bin/STAR \
    && chmod +x /usr/local/bin/STAR \
    && rm -f STAR_${VERSION}.zip \
    && apt-get purge -y --auto-remove wget ca-certificates unzip \
    && rm -rf /var/lib/apt/lists/*

RUN STAR --version

WORKDIR /data
CMD ["STAR"]
