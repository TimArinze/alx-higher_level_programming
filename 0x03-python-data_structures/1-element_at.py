#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > length -1:
        return None
    else:
        for i, s in enumerate(my_list):
            if i == idx:
                return s

