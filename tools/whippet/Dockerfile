ARG VERSION=1.6.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

LABEL org.opencontainers.image.title="Whippet" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.description="Whippet.jl - lightweight and fast quantitative alternative splicing analysis (Julia)" \
      org.opencontainers.image.source="https://github.com/timbitz/Whippet.jl" \
      org.opencontainers.image.licenses="MIT"

ENV JULIA_DEPOT_PATH=/opt/julia-depot \
    JULIA_PROJECT=/opt/Whippet.jl \
    WHIPPET_DIR=/opt/Whippet.jl

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        git \
    && wget -q https://julialang-s3.julialang.org/bin/linux/x64/1.6/julia-1.6.7-linux-x86_64.tar.gz \
        -O /tmp/julia.tar.gz \
    && tar -xzf /tmp/julia.tar.gz -C /opt \
    && ln -s /opt/julia-1.6.7/bin/julia /usr/local/bin/julia \
    && git clone --depth 1 --branch v${VERSION} https://github.com/timbitz/Whippet.jl.git /opt/Whippet.jl \
    && mkdir -p "${JULIA_DEPOT_PATH}" \
    && julia -e 'using Pkg; Pkg.instantiate(); Pkg.precompile()' \
    && chmod -R a+rX "${JULIA_DEPOT_PATH}" /opt/Whippet.jl \
    && apt-get purge -y --auto-remove wget ca-certificates git \
    && rm -rf /var/lib/apt/lists/* /tmp/*

RUN julia -e 'using Whippet; println("Whippet OK")'

WORKDIR /data
CMD ["julia"]
