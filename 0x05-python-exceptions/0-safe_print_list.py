#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0

    try:
        for index in range(0, x):
            print(my_list[index], end="")
            elements += 1;
        print()
        return elements
    except Exception as IndexError:
        print()
        return elements
