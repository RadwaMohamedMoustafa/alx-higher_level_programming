#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        tuple_r = (0, None)
        return tuple_r
    else:
        tuple_r = (length, sentence[0])
        return tuple_r
