#!/bin/bash

# Pull latest master
git pull origin main

# stop old run
docker-compose down

# Run app locally
docker-compose up -d

# Check running container
docker ps