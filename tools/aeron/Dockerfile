FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV VERSION=a6e7d589e3feeb22b5374b455a1a677e3bb2edfa
ENV PATH=/opt/bin/:$PATH


RUN apt update && apt install -y git python3 python3-dev && \
    cd /tmp && \
    git clone https://github.com/SchulzLab/Aeron.git && \
    cd Aeron && \
    git checkout ${VERSION} && \
    cp Binaries/* /opt/bin/ && \
    cp AeronScripts/* /opt/bin/ && \
    chmod +x /opt/bin/*



RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*




