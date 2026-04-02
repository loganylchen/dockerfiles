ARG VERSION=1.9

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        perl \
        r-base \
        python3 \
        samtools \
        wget \
        ca-certificates \
        git \
    && git clone https://github.com/wososa/PSI-Sigma.git /opt/PSI-Sigma \
    && cd /opt/PSI-Sigma && git checkout v${VERSION} || true \
    && chmod +x /opt/PSI-Sigma/*.pl \
    && ln -s /opt/PSI-Sigma/dummyai.pl /usr/local/bin/dummyai.pl \
    && ln -s /opt/PSI-Sigma/PSIsigma.pl /usr/local/bin/PSIsigma.pl \
    && apt-get purge -y --auto-remove wget ca-certificates git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

RUN perl /opt/PSI-Sigma/dummyai.pl --help 2>&1 || true

WORKDIR /data
CMD ["perl", "/opt/PSI-Sigma/dummyai.pl"]
