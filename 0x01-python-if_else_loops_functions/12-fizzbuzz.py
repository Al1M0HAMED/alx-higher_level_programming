#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
            if (i % 3 == 0 and i % 5 == 0):
                status = "FizzBuzz"
            elif (i % 5 == 0):
                status = "Buzz"
            elif (i % 3 == 0):
                status = "Fizz"
            else:
                status = i
            print(status, end=" ")
