#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = []
    sm = 0
    for ele in my_list:
        if ele == search:
            nlist.append(replace)
        else:
            nlist.append(ele)
    return nlist
