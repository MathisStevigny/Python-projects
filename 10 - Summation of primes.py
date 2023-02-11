#Find the sum of all the primes below two million.
totalNumbers = []
total = 0
buffer = 0

for i in range(2000000):
    totalNumbers.append(i)
totalNumbers.remove(0)
totalNumbers.remove(1)
a = totalNumbers[0]

while a < 2000001:
    for i in range(len(totalNumbers)):
        print(totalNumbers)
        buffer = totalNumbers[i] / a
        if buffer == int(buffer):
            totalNumbers.pop(i)
    total += a
    totalNumbers.remove(a)
    a = totalNumbers[0]
    

#while 1 == 1:
#    while a*p < 2000001:
#        totalNumbers.remove(a*p)
#        print(a*p)
#        a += 1
#    
#    total += totalNumbers[0]
#    totalNumbers.pop[0]
#    p = totalNumbers[0]
#    a = 2
#    print(total)