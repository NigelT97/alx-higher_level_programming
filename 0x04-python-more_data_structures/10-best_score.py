#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        mlist = list(a_dictionary.keys())
        sco = 0
        lder = ""
        for i in mlist:
            if a_dictionary[i] > sco:
                sco = a_dictionary[i]
                ldr = i
        return ldr
