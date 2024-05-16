FROM python:3.11.4
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH

RUN pip install git+https://github.com/bartongroup/differr_nanopore_DRS.git@0.2 && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

