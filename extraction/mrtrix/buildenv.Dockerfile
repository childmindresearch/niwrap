FROM ubuntu:20.04

# Disable interactive prompts during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    git \
    python3 \
    python3-pip \
    libeigen3-dev \
    zlib1g-dev \
    qt5-qmake \
    qt5-default \
    libqt5opengl5-dev \
    libqt5svg5* \
    pkg-config \
    less \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Alias python to python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Default command
CMD ["bash"]