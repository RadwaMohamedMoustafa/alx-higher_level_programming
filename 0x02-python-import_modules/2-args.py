#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(arg))
    for i in range(arg):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
