#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copyi = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return copyi
    else:
        copyi[idx] = element
        return copyi
