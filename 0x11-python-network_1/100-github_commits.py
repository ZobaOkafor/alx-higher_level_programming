#!/usr/bin/python3
"""
This script takes your GitHub credentials
(username and personal access token) and uses
the GitHub API to display your id.
"""

import requests
import sys
import base64

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Combine username and password with a colon and encode in Base64
    auth_header = base64.b64encode(f"{username}:{password}".encode()).decode()

    headers = {'Authorization': f'Basic {auth_header}'}
    url = 'https://api.github.com/user'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print(None)
