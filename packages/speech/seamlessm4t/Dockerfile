#---
# name: seamlessm4t
# group: audio
# depends: [fairseq2:0.2.0, pytorch, torchaudio, whisper]
# requires: '>=34.1.0'
# docs: docs.md
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

RUN apt-get update && \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN git clone --depth=1 https://github.com/facebookresearch/seamless_communication /opt/seamlessm4t

WORKDIR /opt/seamlessm4t

RUN pip3 install --no-cache-dir .

RUN /opt/seamlessm4t