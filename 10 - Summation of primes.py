#Find the sum of all the primes below two million.
'''l = []
primes = []
l.append(2)
for i in range(999999):
    l.append((i*2)+3)
print(l[:100])
for i in l:
    primes.append(i)
    print(f"aaaa{i}")
    for j in l:
        if (j%i == 0):
            l.remove(j)
        print(j)
print(sum(primes))'''

'''idea:
a = [2]
int % a[0,1,2,3,...] == 0:
int append a
'''

primes = [2]
count = 3
b = True

while count < 2000000:
    print(count)
    for p in primes:
        if (count/p == int(count/p)):
            b = False
    if (b == True):
        primes.append(count)
    b = True
    count += 2
print(sum(primes))