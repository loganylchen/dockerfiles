###############################################################
# Dockerfile to build container images for leafcutter v0.2.9
# Based on stephanholgerdrukewitz/leafcutter:latest
################################################################

FROM stephanholgerdrukewitz/leafcutter:latest

# File Author / Maintainer
LABEL maintainer="Naoto Kubota <the.owner.of.the.dream123@gmail.com>"
ARG VERSION=0.2.9
# Install classify_clusters.R
WORKDIR /opt/leafcutter/leafcutter/leafcutter/R 
ADD https://raw.githubusercontent.com/davidaknowles/leafcutter/classify_clusters/leafviz/classify_clusters.R .

