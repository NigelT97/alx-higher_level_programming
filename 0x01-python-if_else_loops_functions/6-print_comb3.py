#!/usr/bin/python3
for dn1 in range(0, 10):
    for dn2 in range(dn1 + 1, 10):
        if dn1 == 8 and dn2 == 9:
            print("{}{}".format(dn1, dn2))
        else:
            print("{}{}".format(dn1, dn2), end=", ")
