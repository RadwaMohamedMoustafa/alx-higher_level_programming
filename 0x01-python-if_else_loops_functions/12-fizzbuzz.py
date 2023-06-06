#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 101):
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        if i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i, end=' ')
