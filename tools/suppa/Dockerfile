ARG VERSION=2.4

FROM python:3.4.10-stretch
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/opt/SUPPA:${PATH}"

# Install dependencies
RUN pip install --upgrade pip && \
    pip install scikit-learn numpy pandas scipy statsmodels

WORKDIR /opt
RUN wget https://github.com/comprna/SUPPA/archive/refs/tags/v${VERSION}.zip \
    && unzip v${VERSION}.zip \
    && rm -rf v${VERSION}.zip \
    && mv SUPPA-${VERSION} SUPPA \
    && chmod -R +x SUPPA/*

# Set working directory
WORKDIR /home

# bash
CMD ["bash"]
