#!/usr/bin/python3
"""
This script takes your GitHub credentials
(username and personal access token) and uses
the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner, repository)
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
