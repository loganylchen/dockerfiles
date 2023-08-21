FROM python:3.11.4
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH


RUN pip install numpy openbabel  && \
    pip install meeko && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

