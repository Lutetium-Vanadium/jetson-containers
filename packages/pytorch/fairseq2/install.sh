#!/usr/bin/env bash
set -ex
echo "Building fairseq ${FAIRSEQ2_VERSION}"
   
apt-get update
apt-get install -y --no-install-recommends \
		git \
		libsndfile-dev

rm -rf /var/lib/apt/lists/*
apt-get clean

git clone --branch v${FAIRSEQ2_VERSION} --recursive --depth=1 https://github.com/facebookresearch/fairseq2.git /opt/fairseq2
cd /opt/fairseq2
git checkout v${FAIRSEQ2_VERSION}

# Finally, to install fairseq2’s C++ build dependencies (e.g. cmake, ninja), use:
pip3 install --no-cache-dir -r native/python/requirements-build.txt

cd native
cmake -GNinja -DFAIRSEQ2N_USE_CUDA=ON -B build
cmake --build build

cd python
pip3 install --no-cache-dir .

cd ../..
pip3 install --no-cache-dir .

cd ..
rm -rf /opt/fairseq2

pip3 show fairseq2 && python3 -c 'import fairseq2; print(fairseq2.__version__);'
