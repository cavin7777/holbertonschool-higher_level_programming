#!/usr/bin/python3

""" Module to import JSON """
import json

""" Load from JSON string """


def load_from_json_file(filename):
    """ Load from JSON file and return the object """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
