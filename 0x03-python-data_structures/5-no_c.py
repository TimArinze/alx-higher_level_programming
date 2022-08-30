#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        while 'c' in my_string:
            my_string.remove('c')
        while 'C' in my_string:
            my_string.remove('C')
        return (my_string)
