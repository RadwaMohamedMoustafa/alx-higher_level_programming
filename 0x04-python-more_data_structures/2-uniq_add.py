#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    for el in set(my_list):
        num += el
    return num
