#!/usr/bin/python3
"""
This script takes your GitHub credentials
(username and personal access token) and uses the
GitHub API to display your id.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print(None)
