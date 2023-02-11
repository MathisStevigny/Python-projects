#What is the value of the first triangle number to have over five hundred divisors?
from math import *
startNumber = 0
total = 0
divisors = []
while len(divisors) < 500:
    divisors = []
    startNumber += 1
    for i in range(startNumber):
        total += i
    total = startNumber/2*(1 + startNumber)
    for i in range(ceil(sqrt(total))):
        if total/(i+1) == int(total/(i+1)):
            divisors.append(i+1)
            divisors.append(int(total/(i+1)))
print(divisors)
print(int(total))
print(len(divisors))


#Sn = n/2(u1 + un)