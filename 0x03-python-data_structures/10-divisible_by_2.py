#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list[:]
    for I in range(len(newlist)):
        if I % 2 == 0:
            newlist[I] = True
        else:
            newlist[I] = False
    return newlist
