#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 101):
        msg = " "
        if i % 3 == 0:
            msg = "Fizz"
        if i % 5 == 0:
            msg = "Buzz"
        if i % 15 == 0:
            msg = "FizzBuzz"
        else:
            msg = i
            print(msg, end=' ')
