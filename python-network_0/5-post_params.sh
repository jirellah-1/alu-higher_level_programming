#!/bin/bash
# Sends a POST request with an email and a subject and displays the body of the response.
curl -s -X POST -d "email=test@gmail.com" -d "subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
