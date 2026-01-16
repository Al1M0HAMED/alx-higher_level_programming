#!/usr/bin/python3
"""
7-add_item.py

Module to add all command line arguments to a JSON file.

This script does the following:
1. Ensures the JSON file exists (creates it if it doesn't).
2. Loads the current list from the JSON file if it contains data.
3. Adds all command line arguments (excluding the script name) to the list.
4. Saves the updated list back to the JSON file.

Usage:
    ./7-add_item.py <item1> <item2> ... <itemN>

Modules Imported:
- sys: To access command line arguments.
- os: To check file size and existence.
- 6-load_from_json_file: Custom module to load a list from a JSON file.
- 5-save_to_json_file: Custom module to save a list to a JSON file.
"""

import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
my_list = []

open(filename, "a", encoding="utf-8").close()
if os.stat(filename).st_size != 0:
    my_list = load_from_json_file(filename)

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
