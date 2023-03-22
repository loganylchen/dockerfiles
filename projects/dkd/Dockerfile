FROM ubuntu:22.04

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive



RUN apt update -y && \
    apt -y install python3 python3-dev python3-pip r-base libcurl4-openssl-dev libssl-dev libproj-dev
ADD install_packages_R.R /tmp/
ADD requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt --no-cache-dir && \
    Rscript /tmp/install_packages_R.R && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*