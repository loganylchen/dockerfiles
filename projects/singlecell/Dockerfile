ARG VERSION=1.0

FROM btrspg/vscode-base:0.0.6
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

RUN mkdir -p /tmp/test && \
    cd /tmp/test && \
    wget https://sourceforge.net/projects/mcmc-jags/files/JAGS/4.x/Source/JAGS-4.3.2.tar.gz && \
    tar -zxvf JAGS-4.3.2.tar.gz && \
    cd JAGS-4.3.2 && \
    ./configure && \
    make && \
    make install 


ADD requirements.txt /tmp/
ADD install_packages.R /tmp/
ADD bioconductor_packages.txt /tmp/
ADD devtools_packages.txt /tmp/
ADD CRAN_packages.txt /tmp/


RUN Rscript /tmp/install_packages.R && pip install --no-cache-dir -r /tmp/requirements.txt

RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /data
CMD ["bash"]