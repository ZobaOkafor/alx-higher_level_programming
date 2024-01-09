#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and then saves them to a file.
"""

from sys import argv
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists
if exists(filename):
    # Load existing data from the file
    my_list = load_from_json_file(filename)
else:
    # Create a new list if the file doesn't exist
    my_list = []

# Add arguments to the list
my_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
