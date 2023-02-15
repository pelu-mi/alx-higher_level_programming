#!/bin/bash
# Scipt to send a GET request to a url and display the response body
curl -sI "$1" | grep Location | cut -d '/' -f2
