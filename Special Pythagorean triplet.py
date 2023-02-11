#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
from math import sqrt
sum = 1000
a = 1
b = 2
while 1==1:
    c = sqrt(a**2 + b**2)
    if a+b+c == 1000:
        print(a*b*c)
        print(a,b,c)
        break
    elif a != 1000:
        a += 1
    else:
        a = 1
        b += 1
