#!/usr/bin/python3

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
