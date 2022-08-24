#!/usr/bin/python3
def uppercase(str):
 num =""
 for I in range(len(str)):
   if(str[I] >= 'a' and str[I] <= 'z'):
     num =num + chr(ord(str[I])-32)
     continue
   else:
     num += str[I]
 print("{}".format(num))
  
