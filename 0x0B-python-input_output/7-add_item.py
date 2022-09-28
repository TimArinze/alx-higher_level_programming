#!/usr/bin/python3
"""
A script that adds all arguments to a python list
and then save them to a file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
file_name = "add_item.json"
try:
    my_list = load_from_json_file(file_name)
except FileNotFoundError:
    my_list = []
my_list.extend(args[1:])
save_to_json_file(my_list, file_name)
