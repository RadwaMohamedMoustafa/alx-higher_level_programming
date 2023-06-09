#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for rows in matrix:
            for items in rows:
                print("{:d}".format(items), end=" ")
            print()
