#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    for index in range(0, x):
        try:
            print(my_list[index], end="")
            elements += 1;
        except Exception as IndexError:
            continue
    print("")
    return elements
