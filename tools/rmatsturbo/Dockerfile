ARG VERSION=4.3.0

# rmatsturbo requires R and compiled C extensions — keep ubuntu base for R compat
FROM ubuntu:22.04
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV PATH=/opt/bin/:/opt/rmats/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc g++ gfortran \
        build-essential \
        ca-certificates \
        cmake \
        curl \
        cython3 \
        git \
        libblas-dev \
        libgsl-dev \
        liblapack-dev \
        make \
        python-is-python3 \
        python3-dev \
        python3-pip \
        r-base \
        r-cran-doparallel \
        r-cran-dosnow \
        r-cran-foreach \
        r-cran-getopt \
        r-cran-ggplot2 \
        r-cran-iterators \
        r-cran-mixtools \
        r-cran-nloptr \
        r-cran-rcpp \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
    && mkdir rmats_build && cd rmats_build \
    && git clone https://github.com/Xinglab/rmats-turbo.git \
    && cd rmats-turbo \
    && git checkout v${VERSION} \
    && echo '' > setup_environment.sh \
    && ./build_rmats \
    && mkdir -p /opt/rmats \
    && cp rmats.py cp_with_prefix.py *.so /opt/rmats/ \
    && mkdir -p /opt/rmats/rMATS_C && cp rMATS_C/rMATSexe /opt/rmats/rMATS_C/ \
    && mkdir -p /opt/rmats/rMATS_P && cp rMATS_P/*.py /opt/rmats/rMATS_P/ \
    && mkdir -p /opt/rmats/rMATS_R && cp rMATS_R/*.R /opt/rmats/rMATS_R/ \
    && chmod -R +x /opt \
    && rm -rf /tmp/rmats_build

RUN python3 /opt/rmats/rmats.py --help 2>&1

WORKDIR /data
CMD ["bash"]
