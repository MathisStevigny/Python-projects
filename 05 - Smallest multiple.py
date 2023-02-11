'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

i = 9699690 #multiplication of all primes under 20
divider = 20
testPassed = False

while(testPassed == False):
    if i/divider == int(i/divider):
        divider -= 1
        if (divider == 1):
            testPassed = True
    else:
        divider = 20
        i += 9699690
        #print(i)
    
print(i)
