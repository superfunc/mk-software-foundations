#!/bin/sh

mkdir output

IMAGE_NAME=software_foundations_generator
WRITE_DIR_LOCAL=`pwd`/output
WRITE_DIR_REMOTE=/var/generated

docker build . -t $IMAGE_NAME
docker run -v $WRITE_DIR_LOCAL:$WRITE_DIR_REMOTE -t $IMAGE_NAME
