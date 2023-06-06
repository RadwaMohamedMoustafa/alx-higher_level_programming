#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 101):
        if i % 3 == 0:
            msg = "Fizz"
        if i % 5 == 0:
            msg = "Buzz"
        if i % 15 == 0:
            msg = "FizzBuzz"
        else:
            print(i, end=' ')
