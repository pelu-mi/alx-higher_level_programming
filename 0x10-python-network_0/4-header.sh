#!/bin/bash
# Script to get list of http methods the server will accept
curl -sLH "X-School-User-Id: 98" "$1"
