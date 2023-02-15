#!/bin/bash
# Script to POST using JSON file
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
