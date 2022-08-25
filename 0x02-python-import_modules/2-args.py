#!/usr/bin/python3
import sys
argv = sys.argv
arg_count = len(argv) - 1
if (arg_count == 0):
    print("{:d} arguments.".format(arg_count))
elif (arg_count == 1):
    print("{:d} argument:\n{:d}: {}".format(arg_count, arg_count, argv[1]))
elif (arg_count > 1):
    print("{:d} arguments:".format(arg_count))
    i = 1
    while (i <= arg_count):
        print("{:d}: {:s}".format(i, argv[i]))
        i = i + 1
