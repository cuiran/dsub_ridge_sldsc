#!/bin/bash

docker build --no-cache -t ridge-sldsc .
docker tag ridge-sldsc gcr.io/finucane-dp5/ridge-sldsc:latest
docker push gcr.io/finucane-dp5/ridge-sldsc:latest
