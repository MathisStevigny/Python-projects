'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

maxNumber = 999
numbers = 0 
endNumber = 0  
while numbers <= maxNumber: 
    if (numbers/3) == int(numbers/3) or (numbers/5) == int(numbers/5): 
        endNumber += numbers 
    numbers += 1 

#end result
print(endNumber) 