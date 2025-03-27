FROM btrspg/vscode-base:0.0.3

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive
ARG VERSION



RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip install scTAPE==${VERSION}

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

