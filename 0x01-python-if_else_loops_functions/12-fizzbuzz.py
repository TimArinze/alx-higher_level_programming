#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 == 0 and number % 5 != 0):
            number = 'Fizz'
        elif (number % 5 == 0 and number % 3 != 0):
            number = 'Buzz'
        elif (number % 15 == 0):
            number = 'FizzBuzz'
        print("{}".format(number), end=" ")
