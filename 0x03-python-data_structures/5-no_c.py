#!/usr/bin/python3
def no_c(my_string):
    change = {ord('c') : None, ord('C') : None}
    return (my_string.translate(change))
