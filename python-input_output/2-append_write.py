#!/usr/bin/python3

""" Append in file """


def append_write(filename="", text=""):
    """ Append in file """
    with open(filename, 'a') as f:
        written = f.write(text)
    return written
