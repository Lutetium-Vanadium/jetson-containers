#---
# name: fairseq2
# group: pytorch
# config: config.py
# depends: [pytorch, cmake, ninja]
# test: test.py
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG FAIRSEQ2_VERSION

COPY install.sh /tmp/fairseq2/

RUN /tmp/fairseq2/install.sh
