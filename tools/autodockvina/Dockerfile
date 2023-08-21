FROM python:2.7


ENV PATH=/opt/bin/:/opt/mgltools/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive



RUN apt update && apt install -y wget build-essential gzip libboost-all-dev swig git && \
    cd /tmp && \
    wget https://ccsb.scripps.edu/download/532/ -O test2.tar.gz && \
    tar -zxvf test2.tar.gz && \
    cd mgltools_x86_64Linux2_1.5.7/ && \
    ./install.sh -d /opt/mgltools && \
    cd /tmp && \
    mkdir -p /opt/bin/ && \
    git clone https://github.com/ccsb-scripps/AutoDock-Vina && \
    cd AutoDock-Vina/build/linux/release && \
    make && \
    cp vina vina_split /opt/bin/

ADD setup.py /tmp/AutoDock-Vina/build/python/setup.py
RUN cd /tmp/AutoDock-Vina/build/python && \
    python setup.py build install && \
    cp /tmp/AutoDock-Vina/example/autodock_scripts/*.py /opt/bin/ && \
    chmod +x /opt/bin/*


RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*



