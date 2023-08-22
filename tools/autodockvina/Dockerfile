FROM python:3.8


ENV PATH=/opt/bin/:/opt/mgltools/bin:/opt/adfr/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive
#ENV PYTHONPATH=/opt/mgltools/lib/python2.7


RUN apt update && apt install -y wget build-essential gzip libboost-all-dev swig git ffmpeg libsm6 libxext6 && \
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
    cp vina vina_split /opt/bin/ && \
    cd /tmp && \
    wget https://ccsb.scripps.edu/adfr/download/1028/ -O /tmp/ADFT_install && \
    chmod +x /tmp/ADFT_install && \
    /tmp/ADFT_install --prefix /tmp/adfr --mode silent && \
    cd /tmp/adfr  && \
    tar -zxvf ADFRsuite_x86_64Linux_1.0.tar.gz && \
    cd ADFRsuite_x86_64Linux_1.0 && \
    ./install.sh -d /opt/adfr -c 0 -l && \
    cd /tmp/AutoDock-Vina/build/python && \
    python3 setup.py build install && \
    cd /tmp/AutoDock-Vina/example/autodock_scripts/ && \
    echo $(2to3 -w ./) && \
    cp /tmp/AutoDock-Vina/example/autodock_scripts/*.py /opt/bin/ && \
#    sed -i 's/pythonsh/python3/' /opt/bin/*py && \
    chmod +x /opt/bin/* && \
    cd /tmp && \
    wget https://autodock.scripps.edu/wp-content/uploads/sites/56/2021/10/autodocksuite-4.2.6-x86_64Linux2.tar /tmp/autodocksuite-4.2.6-x86_64Linux2.tar && \
    tar -xvf autodocksuite-4.2.6-x86_64Linux2.tar && \
    cp x86_64Linux2/* /opt/bin/


RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*



