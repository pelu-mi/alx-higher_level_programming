#!/usr/bin/python3
""" Module Documentation
"""


import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Make a list from the args on command line
filename = "add_item.json"
obj = []
arg_list = []
for i in range(1, len(sys.argv)):
    arg_list.append(sys.argv[i])

# If file does not exist
if not os.path.isfile(filename):
    save_to_json_file(arg_list, filename)
else:
    obj = load_from_json_file(filename)
    for item in arg_list:
        obj.append(item)
    save_to_json_file(obj, filename)
