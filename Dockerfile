FROM nvidia/cuda:12.2.0-runtime-ubuntu20.04

# Install system dependencies
RUN <<EOF
  apt-get update 
  # https://stackoverflow.com/a/58264927
  DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata
  # https://stackoverflow.com/a/70866416
  apt-get install -y \
        git wget gcc make vim \
        wget build-essential checkinstall  libreadline-gplv2-dev  libncursesw5-dev  libssl-dev  libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
EOF

RUN <<EOF
 cd /usr/src
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar -xf Python-3.6.5.tgz
cd Python-3.6.5
./configure --enable-optimizations
make install
EOF

# https://stackoverflow.com/a/63457606
RUN pip3 install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt


WORKDIR /workdir

