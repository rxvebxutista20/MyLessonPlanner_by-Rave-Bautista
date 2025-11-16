# Dockerfile using the provided base image
# This template uses a base image that includes FastAPI, React, and Mongo tooling
# Set the image via build-arg or via environment in CI
ARG BASE_IMAGE=fastapi_react_mongo_shadcn_base_image_cloud_arm:release-11112025-1
FROM ${BASE_IMAGE}

# Set environment variables
ARG APP_PORT=3000
ENV APP_PORT=${APP_PORT}

# Create app directory
WORKDIR /app

# If you have a backend or frontend, copy files accordingly. This repo contains static HTML.
# Copy current project files into the image
COPY . /app

# Expose app port
EXPOSE ${APP_PORT}

# Default run - if the base image provides a start server script use it.
# Otherwise, for a static site you can use a lightweight server like 'serve' (node) or 'http-server'.
# Adjust the CMD/ENTRYPOINT to suit your environment.
CMD ["/bin/sh", "-c", "echo 'Customize this Dockerfile: start your backend and frontend here'; sleep infinity"]
