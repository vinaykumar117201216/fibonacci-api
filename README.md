# fibonacci-api

## Overview
This REST API calculates and return the nth of Fibonacci number

## Prerequisites
- Python 3.8+
- Flask

## Installation

git clone https://github.com/vinaykumar117201216/fibonacci-api.git

Install the requirements in requirements.txt, by running something like pip install -r requirements.txt

Then run the api by
python app.py

## Example Usage
curl "http://localhost:5000/fibonacci?n=10"

expected O/P:

{"n":10,"fibonacci":55}

## Containerization

Build and run the docker image by running the following commands at fibonacci-api/Dockerfile

docker build -t fibonacci-api .
docker run -d -p 5000:5000 fibonacci-api

## CI/CD

GitHub actions can be used for the build and deployment proccess

Example GHA workflow: .github/workflows/docker.yml
which automates the build and deployment process, by building image when pushing and deploying to cloudservices like ECS, EKS and AKS

## Monitoring & Logging

basic logging can achived by using python’s logging module

Also, tools like like below can be used for extensive debugging

Sentry for error tracking
Datadog for metrics and logs
AWS CloudWatch for AWS deployments
Azure Monitor for Azure

## Scaling

To handle unexpected and high traffic, ALB or API Gateways can be used

Also, multiple containers can be deployed using EKS, AKS and GKE

Also, serverless options can be conidered like 
AWS Lambda, Azure Functions