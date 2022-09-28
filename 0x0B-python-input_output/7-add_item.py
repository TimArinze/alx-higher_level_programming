#!/usr/bin/python3
"""
A script that adds all arguments to a python list
and then save them to a file
"""


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
file_name = "add_item.json"
my_list = args[1:]

with open(file_name, "a+") as f:
    save_to_json_file(my_list, file_name)
    load_from_json_file(file_name)
