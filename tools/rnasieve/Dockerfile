ARG VERSION=1.0

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --break-system-packages \
        rnasieve

RUN python3 -c "import rnasieve; print('rnasieve OK')"

WORKDIR /data
CMD ["python3"]
