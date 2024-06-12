#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Dgt = number % 10
if number < 0:
    Dgt = -Dgt
if Dgt > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, Dgt))
elif Dgt == 0:
    print("Last digit of {} is {} and is 0".format(number, Dgt))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, Dgt))
