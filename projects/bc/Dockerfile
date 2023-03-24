FROM btrspg/vscode-project-base:main

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive


ADD install_packages_R.R /tmp/
ADD requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt --no-cache-dir && \
    Rscript /tmp/install_packages_R.R && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*
