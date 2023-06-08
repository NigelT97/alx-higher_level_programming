#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    countnum = len(sys.argv) - 1
    if countnum == 0:
        print("0 arguments.")
    elif countnum == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(countnum))
    for i in range(countnum):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
