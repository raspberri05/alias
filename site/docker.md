---
title: Docker
layout: home
---

# Docker

## dbt -> docker build -t

builds a Docker image

required parameters: image-name

## drp -> docker run -p

runs a Docker container

required parameters: port:port image-name

## dps -> docker ps

shows the running containers

required parameters: none

## dpsa -> docker ps -a

shows all containers

required parameters: none

## dst -> docker stop

stops a running container

required parameters: container-id

## drm -> docker rm

removes a container

required parameters: container-id

## drmi -> docker rmi

removes an image

required parameters: image-id

## dei -> docker exec -it

executes a command in a running container

required parameters: container-id /bin/bash

## dcu -> docker-compose up

starts the Docker Compose services

required parameters: none

## dcd -> docker-compose down

stops the Docker Compose services

required parameters: none

## dcp -> docker-compose ps

shows the Docker Compose services

required parameters: none

## dcl -> docker-compose logs

shows the logs of the Docker Compose services

required parameters: none

## dnetpr -> docker network prune

Remove all unused networks

required parameters: none

## dvolpr -> docker volume prune

Remove unused local volumes

required parameters: none

## dconpr -> docker container prune

Remove all stopped containers

required parameters: none

## dimgpr -> docker image prune

Remove unused images

required parameters: none

## dimgpra -> docker image prune -a

Remove all unused images, not just dangling ones

required parameters: none

