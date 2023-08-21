FROM mambaorg/micromamba:1.4.9
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH


RUN micromamba create -n meeko -c conda-forge openbabel numpy   && \
    micromamba activate meeko && \
    pip install meeko && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*
