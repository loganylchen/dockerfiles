FROM python:3.11.4
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH

ADD https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static /opt/bin/bedtools
RUN pip install LAFITE==1.0.2 && \
    chmod +x /opt/bin/* && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

