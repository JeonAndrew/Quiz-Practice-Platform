# Use an official Ubuntu image as the base
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install dependencies for C++ development, Git, CMake, and Clang-Tidy
RUN apt-get update && \
    apt-get install -y \
    clang \
    git \
    make \
    cmake \
    clang-tidy \
    libboost-all-dev \
    && apt-get clean

# Install Catch2 from the package manager
RUN apt-get update && apt-get install -y \
    catch2 \
    && rm -rf /var/lib/apt/lists/*

# Set the default command to open a shell
CMD ["/bin/bash"]