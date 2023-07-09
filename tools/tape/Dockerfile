FROM btrspg/vscode-base:latest

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive




RUN pip install torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 --index-url https://download.pytorch.org/whl/cpu && \
    pip install scTAPE==1.1.2

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

