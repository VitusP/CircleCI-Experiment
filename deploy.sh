#!/bin/bash

# Pull latest master
git pull origin main

# stop old run
docker compose -f compose.yml -f production.yml stop

# Run app locally
docker compose -f compose.yml -f production.yml up -d --build

# Check running container
docker ps