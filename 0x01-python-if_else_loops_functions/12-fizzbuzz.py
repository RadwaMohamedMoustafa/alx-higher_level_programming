#!/usr/bin/python3
def fizzbuzz():
    msg = ''
    for i in range(0, 101):
        if i % 15 == 0:
            msg = 'FizzBuzz'
        if i % 5 == 0:
            msg = 'Buzz'
        if i % 3 == 0:
            msg = 'Fizz'
        else:
            msg = i
            print(msg, end=' ')
