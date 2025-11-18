FROM ubuntu:22.04

ENV PATH=/opt/SpliceTools/bin:/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt update -y \
    &&  apt -y install  \
    python3-pip \
    python3-dev \
    git \
    libparallel-forkmanager-perl \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 10 \
    && git clone https://github.com/flemingtonlab/SpliceTools.git /opt/SpliceTools/ \
    && cd /opt/SpliceTools/ \
    && git checkout v${VERSION}  \
    && sed -i 's/split_line !=/split_line < /' /opt/SpliceTools/bin/*.pl \
    && sed -i 's/>chr/>/' /opt/SpliceTools/bin/*.pl 



ADD requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt \
    # Remove build dir
    && apt autoremove && apt clean && apt autoclean && rm -rf /tmp/*
