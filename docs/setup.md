# Setup Guide for cheminformatics-environment

Welcome to the setup guide for `cheminformatics-environment`. This guide will walk you through the steps to get your cheminformatics environment running in a Docker container.

## 1. Prerequisite

Before proceeding, ensure you have the following installed:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/downloads) (for cloning the repository)

If hosting on cloud server, such as AWS, GPC, or Azure, please make an account and make sure you have all the appropriate permissions.

## 2. Local Development

### Setup

* Clone repository to your local drive

```bash
# Clone repository
git clone git@github.com:gabenavarro/cheminformatics-environment.git
# Jump into repository
cd ./cheminformatics-environment
```

* Build docker image from docker file

```bash
# Build image
docker build -f Dockerfile.dev -t cheminformatics-environment:dev .
```

* Run the docker container from docker image

```bash
# Run container
docker run -d \
  --name cheminformatics-environment-dev \
  -v $(pwd)/:/app/ \
  cheminformatics-environment:dev
```


### Rebuilding

In case you need to rebuild your docker image, follow these commands

```bash
# Stop and remove current container
docker stop cheminformatics-environment-dev \
&& docker rm cheminformatics-environment-dev \
# Re build docker image 
&& docker build -f Dockerfile.dev -t cheminformatics-environment:dev . \
# Run image container
&& docker run -d \
  --name cheminformatics-environment-dev \
  -v $(pwd)/:/app/ \
  cheminformatics-environment:dev
```