#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and then saves them to a file.
"""

import json
from sys import argv
from os.path import exists

filename = "add_item.json"

# Check if the file exists
if exists(filename):
    # Load existing data from the file
    with open(filename, mode="r", encoding="utf-8") as file:
        my_list = json.load(file)
else:
    # Create a new list if the file doesn't exist
    my_list = []

# Add arguments to the list
my_list.extend(argv[1:])

# Save the updated list to the file
with open(filename, mode="w", encoding="utf-8") as file:
    json.dump(my_list, file)
