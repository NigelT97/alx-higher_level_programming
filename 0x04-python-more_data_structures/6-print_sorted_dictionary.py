#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictioanry,keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
