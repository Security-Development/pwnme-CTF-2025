#!/bin/sh

docker build -t einstein .
docker run --privileged -p 1337:1337 -it einstein
