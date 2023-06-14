#!/usr/bin/python3
def uniq_add(my_list=[]):
    nlist = []
    sm = 0
    for nm in my_list:
        if nm not in nlist:
            sm += nm
            nlist.append(nm)
    return sm
