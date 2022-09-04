#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None:
        new = sorted(a_dictionary)
        return new[-1]
    else:
        return None
