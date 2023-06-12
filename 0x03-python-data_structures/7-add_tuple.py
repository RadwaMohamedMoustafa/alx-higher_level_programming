#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    a = tuple_a[:2] + tuple_c
    b = tuple_b[:2] + tuple_c
    tuple_c = (a[0] + b[0], a[1] + b[1])
    return tuple_c
