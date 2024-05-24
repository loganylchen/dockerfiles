FROM mambaorg/micromamba:1.5

ARG EPINANO_VERSION=1.2.3

ENV PATH "${PATH}:/opt/Epinano/:/opt/conda/bin/"
ENV SAM2TSV "/opt/Epinano/misc/sam2tsv.jar"
ENV LC_ALL=en_US.utf8
ENV LANG=en_US.utf8
USER root
WORKDIR /opt/

RUN /usr/bin/micromamba install -y -c conda-forge -n base wget openjdk=20.0.0 samtools && \
    /usr/bin/micromamba create -y -c conda-forge -n epinano python=3.6.7  && \
    /usr/bin/micromamba run -n epinano pip install requests paho-mqtt \
                                                    atomicwrites==1.4.0 attrs==21.2.0 biopython==1.76 cloudpickle==1.3.0 \
                                                    dask==2.5.2 fsspec==2021.6.1 future==0.17.1 h5py==2.10.0  \
                                                    importlib-metadata==4.6.1 locket==0.2.1  more-itertools==8.8.0  \
                                                    numpy==1.17.2 pandas==0.24.2 partd==1.2.0 pluggy==0.13.1  \
                                                    py==1.10.0 pysam==0.15.4 pytest==4.4.1 python-dateutil==2.8.1 \
                                                    pytz==2021.1 scikit-learn==0.20.2 scipy==1.5.4 six==1.16.0  \
                                                    toolz==0.11.1 typing-extensions==3.10.0.0 zipp==3.5.0 && \
    /usr/bin/micromamba create -y -c conda-forge -c r -n r r-base=3.6 r-rcurl r-outliers r-reshape2 \
	r-ggplot2 r-car r-ggrepel r-tidyverse r-optparse && \
    echo -e '#!/bin/bash\n/usr/bin/micromamba run -n epinano python "$@"' > /usr/bin/python && \
    chmod +x /usr/bin/python && \
    echo -e '#!/bin/bash\n/usr/bin/micromamba run -n r Rscript "$@"' > /usr/bin/Rscript && \
    chmod +x /usr/bin/Rscript && \
    wget https://github.com/novoalab/EpiNano/archive/refs/tags/EpiNano${EPINANO_VERSION}.tar.gz && \
    tar -zvxf EpiNano${EPINANO_VERSION}.tar.gz && \
    mv EpiNano-EpiNano${EPINANO_VERSION} Epinano && \
    chmod +x /opt/Epinano/*.py && \
    rm -rf EpiNano${EPINANO_VERSION}.tar.gz && \
    /usr/bin/micromamba clean --all --yes







