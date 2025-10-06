#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        print("Element at index {:d} is None".format(idx))
    if idx > len(my_list):
        print("Element at index {:d} is None".format(idx))
    for i in range(len(my_list)):
        return (my_list[idx])
