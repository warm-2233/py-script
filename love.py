# print(
#    '\n'.join(
      
#       ['|'.join(
#             [
#             ('-Love-'[(x-y)%6]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else'+')for x in range(-30,30)
#             ]
#          )for y in range(15,-15,-1)]
#       )
#    )

import sys


a=" love you"
e = ' '
if len(sys.argv) == 2:
   a= sys.argv[1]

l=len(a)
s="\n"

w = []
for y in range(15,-15,-1):
   w1 = []
   for x in range(-30,30):
      q = (a[(x-y)%l] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else e)
      w1.append(q)

   w.append("".join(w1))

s=s.join(w)

print(s)
input()