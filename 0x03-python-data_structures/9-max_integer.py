#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = my_list[0]
    if my_list:
        for number in my_list:
            if number > max_val:
                max_val = number
    else:
        return None
    return max_val
