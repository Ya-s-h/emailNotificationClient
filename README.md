# Flask-Discord-Notifier

A lightweight Flask-based microservice that listens to HTTP POST requests and sends notifications to Discord when a change is detected.

## Overview

This application receives HTTP POST requests at the `/notificationClient` endpoint. When a POST request is received, the application checks for a `validationToken` in the request parameters. If a `validationToken` is found, the application returns the `validationToken` back in the response. 

If a `validationToken` is not found, the application expects to receive a JSON payload with a `value` key, which is an array of change notifications. It will extract the first change notification and send a message to a configured Discord webhook URL. This message will notify that a change has occurred in the monitored resource.

The application is designed to be run in a Docker container for ease of deployment and scalability.

## Technologies Used
- Flask (a lightweight WSGI web application framework)
- Docker (for creating and managing the application deployment)
- Python's built-in `requests` library for making HTTP requests to Discord

## Deployment
Instructions for building and deploying the Docker container are provided. The application is set to run on port 3000 within the Docker container and this port is exposed for use by other services. 

## Usage
The primary use case for this application is to monitor changes to a resource and send notifications of changes to a Discord channel.

*Please note that you would need to replace the placeholder Discord webhook URL in the code with your actual Discord webhook URL before using this application.*
