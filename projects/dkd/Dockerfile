ARG VERSION=1.0

FROM btrspg/vscode-base:0.0.1
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ADD install_packages_R.R /tmp/
ADD requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt --no-cache-dir && \
    Rscript /tmp/install_packages_R.R && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /data
CMD ["bash"]
