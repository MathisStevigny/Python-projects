#What is the 10 001st prime number?
count = 2
primes = [2,3]
number = 4
primePos = 0
while count < 20000:
    try:
        if number/primes[primePos] == int(number/primes[primePos]):
            number += 1
            primePos = 0
        else:
            primePos += 1
            continue
    except IndexError:
        primes.append(number)
        print(number)
        count += 1
        primePos = 0
        number += 1
print(primes)
