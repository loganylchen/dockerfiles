ARG VERSION=2a

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH=/opt/iupred2a:$PATH

ADD ./iupred2a.tar.gz /tmp/

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
    && mv /tmp/iupred2a /opt/iupred2a \
    && chmod -R +x /opt/iupred2a \
    && rm -rf /var/lib/apt/lists/*

RUN python3 /opt/iupred2a/iupred2a.py 2>&1 | head -3 || true

WORKDIR /data
CMD ["python3", "/opt/iupred2a/iupred2a.py"]
