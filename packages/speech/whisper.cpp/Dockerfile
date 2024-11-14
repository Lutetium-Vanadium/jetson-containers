#---
# name: whisper.cpp
# group: audio
# depends: cuda
# requires: '>=34.1.0'
# docs: docs.md
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG WHISPER_MODEL=small

WORKDIR /opt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  libsdl2-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Clone the repository:
RUN git clone https://github.com/ggerganov/whisper.cpp --depth=1

WORKDIR /opt/whisper.cpp

RUN make -j $WHISPER_MODEL && \
    GGML_CUDA=1 make -j

ENTRYPOINT ./stream -m ./models/$WHISPER_MODEL.bin -t 4 8 --step 500 --length 5000