# Use the official Python 3.12 image as the base
FROM python:3.12-slim

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies (e.g., curl, git, nano, etc.)
RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    curl \
    git \
    nano \
    vim \
    wget \
    python3-venv && \
    apt-get clean

# Install Node.js and npm for React development
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install --yes nodejs && \
    npm install -g npm@latest && \
    apt-get clean

# Install Python packages commonly used for development
RUN pip install --no-cache-dir \
    flask \
    requests

# Expose port 3000 for React
EXPOSE 3000

# Expose port 8080 for backend
EXPOSE 8080

# Set the default command to open a shell
CMD ["/bin/bash"]
