#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndict = {}
    for key, value in a_dictionary.items():
        ndict.update({key: (value * 2)})
    return ndict
