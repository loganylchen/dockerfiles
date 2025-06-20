FROM btrspg/vscode-base:0.0.6

RUN mkdir -p /tmp/test && \
    cd /tmp/test && \
    wget https://sourceforge.net/projects/mcmc-jags/files/JAGS/4.x/Source/JAGS-4.3.2.tar.gz && \
    tar -zxvf JAGS-4.3.2.tar.gz && \
    cd JAGS-4.3.2 && \
    ./configure && \
    make && \
    make install 



ADD install_packages.R /tmp/
ADD bioconductor_packages.txt /tmp/
ADD devtools_packages.txt /tmp/
ADD CRAN_packages.txt /tmp/


RUN Rscript /tmp/install_packages.R 

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*