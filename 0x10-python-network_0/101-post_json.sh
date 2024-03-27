#!/bin/bash
# This script sends a JSON POST request to a URL with a given JSON file.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
