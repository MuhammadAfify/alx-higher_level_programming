#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstDgt = number % 10
if lstDgt > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lstDgt))
elif lstDgt == 0:
    print("Last digit of {} is {} and is 0".format(number, lstDgt))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lstDgt))
