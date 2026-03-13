FROM debian:bookworm-slim

ENV PATH=/opt/bin:/opt/PUREE:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION=5a0a702535e79e37b071971063e72fa697540818

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/skandlab/PUREE.git /opt/PUREE_repo \
    && cd /opt/PUREE_repo \
    && git checkout ${VERSION} \
    && pip3 install --no-cache-dir --break-system-packages -r requirements.txt \
    && rm -rf /opt/PUREE_repo/.git

ADD PUREE /opt/PUREE/

RUN chmod -R +x /opt/PUREE \
    && python3 -c "print('PUREE deps OK')"

WORKDIR /data
CMD ["bash"]
