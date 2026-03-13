FROM debian:bookworm-slim

ENV PATH=/opt/SpliceTools/bin:/opt/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip \
        git \
        libparallel-forkmanager-perl \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/loganylchen/SpliceTools.git /opt/SpliceTools \
    && cd /opt/SpliceTools \
    && git checkout ${VERSION} \
    && sed -i 's/split_line !=/split_line < /' /opt/SpliceTools/bin/*.pl \
    && sed -i 's/>chr/>/' /opt/SpliceTools/bin/*.pl

ADD requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir --break-system-packages -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

RUN python3 -c "import pandas, matplotlib, seaborn; print('deps OK')"

WORKDIR /data
CMD ["bash"]
