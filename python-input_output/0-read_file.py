#!/usr/bin/python3

""" Read file"""

def read_file(filename=""):
    """ Read file """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
