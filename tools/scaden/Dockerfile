FROM btrspg/vscode-base:0.0.3

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive




RUN pip install scaden

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

