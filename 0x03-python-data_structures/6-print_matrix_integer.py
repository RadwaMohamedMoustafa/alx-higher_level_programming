#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for rows in matrix:
            r_len = len(rows)
            for items in range(r_len):
                end_s = ' ' if items != r_len - 1 else ''
                print("{:d}".format(rows[items]), end=end_s)
            print()
