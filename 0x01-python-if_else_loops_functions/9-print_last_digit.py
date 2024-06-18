#!/usr/bin/python3
def print_last_digit(number):
    lstdgt = abs(number) % 10
    print("{}".format(lstdgt), end="")
    return lstdgt
