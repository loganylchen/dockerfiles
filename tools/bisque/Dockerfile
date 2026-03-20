ARG VERSION=1.0

FROM btrspg/vscode-base:0.0.3
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive

ADD install_packages_R.R /tmp/

RUN Rscript /tmp/install_packages_R.R \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /data
CMD ["R"]
