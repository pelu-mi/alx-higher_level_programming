#!/bin/bash
# Script to POST using JSON file
curl -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
