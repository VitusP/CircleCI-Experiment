# CircleCI-Experiment
Repository to checkout features of CircleCi

## Prod Deployment
```Shell
# Deploy in production
docker compose -f compose.yml -f production.yml up -d --build

# Stop in production
docker compose -f compose.yml -f production.yml stop
```

## Local deployment
```Shell
# Local deployment
docker compose -f compose.yml up -d --build

# Stop in production
docker compose -f compose.yml down --volumes
```