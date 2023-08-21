FROM ubuntu:22.04


ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive



RUN apt update && apt install -y wget build-essential gzip && \
    cd /tmp && \
    mkdir -p /opt/bin/ && \
    wget https://vina.scripps.edu/wp-content/uploads/sites/55/2020/12/autodock_vina_1_1_2_linux_x86.tgz && \
    tar -zxvf autodock_vina_1_1_2_linux_x86.tgz && \
    cp autodock_vina_1_1_2_linux_x86/bin/* /opt/bin/

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*



