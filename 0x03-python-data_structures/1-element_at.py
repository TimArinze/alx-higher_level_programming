#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > length:
        return None
    elif 0 <= idx < length:
        for i, s in enumerate(my_list):
             if i == idx:
                return s
    else:
        return None

