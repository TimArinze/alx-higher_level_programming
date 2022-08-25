#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv)
    add = 0
    for number in argv[1:]:
        add += int(number)
    print("{:d}".format(add))
