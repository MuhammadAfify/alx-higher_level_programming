#!/usr/bin/python3
def remove_char_at(str, n):
    NewStr = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            NewStr += str[i]
    return NewStr
