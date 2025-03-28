FROM btrspg/vscode-base:0.0.3

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION



RUN pip install scaden==${VERSION}

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

