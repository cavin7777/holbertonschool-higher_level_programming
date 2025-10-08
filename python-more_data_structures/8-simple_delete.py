#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    for i in (a_dictionary.keys()):
        if i == key:
            a_dictionary.pop(i)
        else:
            a_dictionary
        return a_dictionary