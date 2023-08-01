FROM btrspg/vscode-base:0.0.3

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive



RUN pip install LAFITE==1.0.3
ADD https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static /opt/bin/bedtools
RUN chmod +x /opt/bin/* && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

