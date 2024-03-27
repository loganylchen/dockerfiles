FROM python:3.11.4
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH

RUN pip install git+git@github.com:bartongroup/differr_nanopore_DRS.git && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

