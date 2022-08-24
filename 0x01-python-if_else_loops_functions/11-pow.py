#!/usr/bin/python3
def pow(a, b):
 num = a**b
 num = int(num)
 if num < 0:
 return(-num)
 else:
 return(num)
