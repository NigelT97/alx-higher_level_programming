#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lkeys = list(a_dictionary.keys())
    for vdic in lkeys:
        if value == a_dictionary.get(vdic):
            del a_dictionary[vdic]
    return (a_dictionary)
