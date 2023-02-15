#!/bin/bash
# Script to send a post request to the passed url
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
