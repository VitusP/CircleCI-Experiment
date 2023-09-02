#!/bin/bash

# git pull
git pull

# stop old run
docker compose -f compose.yml down --volumes

# Run app locally
docker compose -f compose.yml up -d --build

# Check running container
docker ps