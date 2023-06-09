#!/usr/bin/python3

def no_c(my_string):

    let = "c"
    let2 = "C"
    new_string = ""
    length = len(my_string)
    for char in my_string:
        if char != let and char != let2:
            new_string += char

    return new_string
