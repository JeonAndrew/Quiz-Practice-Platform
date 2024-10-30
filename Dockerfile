# Use an official Ubuntu image as the base
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install dependencies for C++ development, Git, CMake, Clang-Tidy, among other useful packages
RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    clang \
    build-essential \
    ca-certificates \
    curl \
    git \
    lld \
    valgrind \
    gdb \ 
    lldb \
    make \
    cmake \
    clang-tidy \
    libboost-all-dev \
    nano \
    vim \
    wget \
    && apt-get clean

# Install Catch2 from the package manager
RUN apt-get update && apt-get install -y \
    catch2 \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm for React development
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

# Install Crow C++ web framework

RUN git clone https://github.com/acopar/crow  && \
    cd crow && \
    make install

# Expose port 3000 for React
EXPOSE 3000

# Set the default command to open a shell
CMD ["/bin/bash"]