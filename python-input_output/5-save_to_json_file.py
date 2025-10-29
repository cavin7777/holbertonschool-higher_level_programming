#!/usr/bin/python3

""" Module to import JSON """
import json

""" Save to JSON string """


def save_to_json_file(my_obj, filename):
    """ Save to JSON string """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
