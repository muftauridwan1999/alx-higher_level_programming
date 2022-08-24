#!/usr/bin/python3
def fizzbuzz():
 for I in range(101)
   if (I % 3 == 0 and I % 5 == 0):
      print("FizzBuzz", end = ' ')
   elif (I % 3 == 0):
      print("Fizz", end = ' ')
   elif (I % 5 == 0):
      print("Buzz", end = ' ')
   else:
      print(I)
