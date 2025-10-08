#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary == {}:
        a_dictionary.keys = key
        a_dictionary.values = value

    for i in a_dictionary.keys():
        if i == key:
            a_dictionary[i] = value
        else:
            i = key
            a_dictionary[i] = value
        return a_dictionary
