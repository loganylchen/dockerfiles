FROM btrspg/vscode-base:0.0.3

ENV PATH=/opt/bin/:$PATH
ENV DEBIAN_FRONTEND=noninteractive




RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip install scTAPE==1.1.2

RUN apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*

