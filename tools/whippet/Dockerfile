ARG VERSION=1.6.1

FROM debian:bookworm-slim AS builder
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
    && git clone https://github.com/timbitz/Whippet.jl.git /opt/Whippet.jl \
    && cd /opt/Whippet.jl && git checkout v${VERSION} || true \
    && julia --project=/opt/Whippet.jl -e 'using Pkg; Pkg.instantiate()' \
    && rm -rf /tmp/*

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

COPY --from=builder /opt/julia-1.9.4 /opt/julia-1.9.4
COPY --from=builder /opt/Whippet.jl /opt/Whippet.jl
COPY --from=builder /root/.julia /root/.julia

RUN ln -s /opt/julia-1.9.4/bin/julia /usr/local/bin/julia

ENV WHIPPET_DIR=/opt/Whippet.jl

RUN julia --project=/opt/Whippet.jl -e 'using Whippet; println("OK")' 2>&1 | tail -1

WORKDIR /data
CMD ["julia"]
