#!/usr/bin/python3

""" Write in file """

def write_file(filename="", text=""):
    """ Write in file """
    with open(filename, 'w') as f:
        written = f.write(text)
    return written
