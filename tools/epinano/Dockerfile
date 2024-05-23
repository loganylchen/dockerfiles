## this will do biocorecrg/mopepinano:0.2
FROM biocorecrg/centos-perlbrew-pyenv3-java:centos7

# File Author / Maintainer
MAINTAINER Luca Cozzuto <lucacozzuto@gmail.com>

ARG EPINANO_VERSION=1.2.3

ENV PATH "${PATH}:/opt/Epinano${EPINANO_VERSION}/"
ENV SAM2TSV "/opt/Epinano${EPINANO_VERSION}/misc/sam2tsv.jar"
ENV LC_ALL=en_US.utf8
ENV LANG=en_US.utf8

WORKDIR /opt/

#upgrade pip
RUN pip install -U pip && \
    pip install --upgrade setuptools && \
    yum install -y wget && \
    pip install requests paho-mqtt && \
    pip install atomicwrites==1.4.0 attrs==21.2.0 biopython==1.76 cloudpickle==1.3.0 && \
    pip install dask==2.5.2 fsspec==2021.6.1 future==0.17.1 \
    h5py==2.10.0 importlib-metadata==4.6.1 && \
    pip install locket==0.2.1  more-itertools==8.8.0 numpy==1.17.2 pandas==0.24.2 && \
    pip install partd==1.2.0 pluggy==0.13.1 py==1.10.0 pysam==0.15.4 pytest==4.4.1 python-dateutil==2.8.1 && \
    pip install pytz==2021.1 \
    scikit-learn==0.20.2 scipy==1.5.4 six==1.16.0 toolz==0.11.1 typing-extensions==3.10.0.0 zipp==3.5.0 && \
    wget https://github.com/novoalab/EpiNano/archive/refs/tags/EpiNano${EPINANO_VERSION}.tar.gz && \
    tar -zvxf *.tgz; rm *.tar.gz && \
    chmod +x /opt/Epinano${EPINANO_VERSION}/*.py && \
    yum clean all && \
    rm -fr *.tar.gz; rm -fr *.bz2; rm -fr ./tmp && \
    rm -rf /var/cache/yum







