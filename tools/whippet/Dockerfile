ARG VERSION=1.6.1

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        git \
    && wget -q https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.4-linux-x86_64.tar.gz \
        -O /tmp/julia.tar.gz \
    && tar -xzf /tmp/julia.tar.gz -C /opt \
    && ln -s /opt/julia-1.9.4/bin/julia /usr/local/bin/julia \
    && git clone --depth 1 --branch v${VERSION} https://github.com/timbitz/Whippet.jl.git /opt/Whippet.jl \
    && rm -f /opt/Whippet.jl/Manifest.toml \
    && julia --project=/opt/Whippet.jl -e 'using Pkg; Pkg.resolve(); Pkg.instantiate()' \
    && apt-get purge -y --auto-remove wget ca-certificates git \
    && rm -rf /var/lib/apt/lists/* /tmp/*

ENV WHIPPET_DIR=/opt/Whippet.jl

RUN julia --project=/opt/Whippet.jl -e 'using Whippet; println("Whippet OK")'

WORKDIR /data
CMD ["julia"]
