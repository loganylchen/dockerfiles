ARG VERSION=5.0b

FROM debian:bookworm-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION
ENV PATH=/opt/signalp/bin:$PATH

ADD ./signalp-5.0b.Linux.tar.gz /tmp/

RUN mv /tmp/signalp-5.0b /opt/signalp \
    && chmod -R +x /opt/signalp

RUN /opt/signalp/bin/signalp -h 2>&1

WORKDIR /data
CMD ["signalp"]
