#!/usr/bin/python3

"""Prints numbers from 1 to 100 separated by a space.
   For multiples of 3 print Fizz, for 5 print Buzz.
   For multiples of both 3 and 5 print FizzBuzz.
   """


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
