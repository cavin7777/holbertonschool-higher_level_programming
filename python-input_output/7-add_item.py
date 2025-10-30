#!/usr/bin/python3

""" Module to import JSON """
import json
import sys

""" Load, add and save from JSON string """
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
	items = load_from_json_file("add_item.json")
except Exception:
	items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
save_to_json_file(items, "add_item.json")
