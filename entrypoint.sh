#!/bin/bash

# Check if migrations directory already exists
if [ -d "migrations" ]; then
  echo "Migrations directory already exists."
else
  # Initialize migration directory
  python src/manage.py db_init
fi

# Perform the database migration
python src/manage.py db_migrate
python src/manage.py db_upgrade

# Start the Flask app
python src/controller.py