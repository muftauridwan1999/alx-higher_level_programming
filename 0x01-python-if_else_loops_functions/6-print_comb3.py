#!/usr/bin/python3
for I in range(0, 90):
 if I % 10 == 0:
   continue
 elif I % 2 == 1:
   continue
 else:
  print("{:02d}".format(I), end = ', ')
