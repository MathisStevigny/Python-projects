#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
number = 600851475143
test = 1
largestFound = 0
while number != 1:
    if number/test == int(number/test):
        largestFound = test
        print(largestFound)
        number /= test
    test += 1
print(largestFound)

