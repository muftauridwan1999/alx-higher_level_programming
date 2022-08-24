#!/usr/bin/python3

def print_last_digit(number):
 num = repr(number)
 num = num[-1]
 num = int(num)
 print("{}".format(num))
 return num
