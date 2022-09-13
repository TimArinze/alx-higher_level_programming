#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            elements += 1
        except BaseException:
            continue
    print()
    return elements
