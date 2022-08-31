#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        my_list.sort()
        i, add = 1, my_list[0]
        while i in range(len(my_list)):
            if my_list[i] != my_list[i - 1]:
                add = add + my_list[i]
            i = i + 1
        return (add)
