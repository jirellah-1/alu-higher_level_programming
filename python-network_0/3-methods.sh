#!/bin/bash
# Displays all the HTTP methods the server accepts for a URL.
curl -sI -X OPTIONS "$1" | grep -i '^allow:' | cut -d ' ' -f2- | tr -d '\r'
