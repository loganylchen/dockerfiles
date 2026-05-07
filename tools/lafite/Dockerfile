ARG VERSION=1.0.3

FROM python:3.11-slim
LABEL maintainer="Yuelong CHEN <yuelong.chen.btr@gmail.com>"

ARG VERSION

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/bin:$PATH

# Install system dependencies and bedtools
# git needed for VERSION=1.0.3 install path (tagged on GitHub but never
# published to PyPI despite the release name claiming so).
RUN apt-get update && apt-get install -y --no-install-recommends \
        bedtools \
        git \
    && rm -rf /var/lib/apt/lists/*

# Install LAFITE and dependencies. 1.0.3 only exists as a GitHub tag
# (PyPI tops out at 1.0.2), so install from git for that version.
RUN case "${VERSION}" in \
         1.0.3) pip install --no-cache-dir \
                  "git+https://github.com/TF-Chan-Lab/LAFITE.git@${VERSION}" ;; \
         *)     pip install --no-cache-dir "LAFITE==${VERSION}" ;; \
       esac

# Verify installation
RUN lafite --help 2>&1

WORKDIR /data
CMD ["lafite"]
