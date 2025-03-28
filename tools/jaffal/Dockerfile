FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV VERSION=2.3
ENV PATH=/opt/bin/:$PATH
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN apt update && apt install -y wget build-essential g++ zlib1g-dev libbz2-dev liblzma-dev openjdk-8-jdk python3 r-base r-base-dev git && \
    mkdir -p /opt/bin /opt/softwares && \
    cd /tmp && \
    git clone https://github.com/lh3/seqtk.git && \
    cd seqtk &&  make && \
    cp seqtk /opt/bin/ && \
    cd /tmp/ && \
    wget https://github.com/Oshlack/JAFFA/releases/download/version-${VERSION}/JAFFA-version-${VERSION}.tar.gz && \
    tar -zxvf JAFFA-version-${VERSION}.tar.gz && \
    g++ -O3 -o /opt/bin/extract_seq_from_fasta JAFFA-version-${VERSION}/src/extract_seq_from_fasta.c++ && \
    g++ -std=c++11 -O3 -o /opt/bin/make_simple_read_table JAFFA-version-${VERSION}/src/make_simple_read_table.c++ && \
    g++ -std=c++11 -O3 -o /opt/bin/make_3_gene_fusion_table JAFFA-version-${VERSION}/src/make_3_gene_fusion_table.c++ && \
    cd /tmp && \
    cp -r JAFFA-version-${VERSION} /opt/softwares/JAFFA

COPY process_transcriptome_align_table.c++ /tmp/

RUN g++ -std=c++11 -O3 -o /opt/bin/process_transcriptome_align_table /tmp/process_transcriptome_align_table.c++ 

RUN chmod +x /opt/bin/* && \
    apt autoremove && \
    apt clean && \
    apt autoclean && \
    rm -rf /tmp/*


