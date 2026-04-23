ARG VERSION=2.3

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="PSI-Sigma" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="PSI-Sigma - alternative splicing analysis with statistical testing" \
      org.opencontainers.image.source="https://github.com/wososa/PSI-Sigma" \
      org.opencontainers.image.licenses="MIT"

RUN apt-get update && apt-get install -y --no-install-recommends \
        perl \
        cpanminus \
        build-essential \
        pkg-config \
        libgsl-dev \
        pdl \
        r-base \
        python3 \
        samtools \
        git \
        ca-certificates \
    && git clone --depth 1 --branch v${VERSION} https://github.com/wososa/PSI-Sigma.git /opt/PSI-Sigma \
        || git clone --depth 1 https://github.com/wososa/PSI-Sigma.git /opt/PSI-Sigma \
    && chmod +x /opt/PSI-Sigma/*.pl \
    && cpanm --notest \
        PDL::LiteF \
        PDL::GSL::CDF \
        PDL::Stats \
        Statistics::Multtest \
        Statistics::R \
    && for pl in /opt/PSI-Sigma/*.pl; do ln -sf "$pl" /usr/local/bin/$(basename "$pl"); done \
    && apt-get purge -y git \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN perl -e "use PDL::LiteF; use PDL::GSL::CDF; use PDL::Stats; use Statistics::Multtest; use Statistics::R; print qq(OK\n)"

WORKDIR /data
CMD ["perl", "/opt/PSI-Sigma/dPSI.pl"]
