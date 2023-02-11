maxNumber = 999
numbers = 0 
endNumber = 0  
while numbers <= maxNumber: 
    if (numbers/3) == int(numbers/3) or (numbers/5) == int(numbers/5): 
        endNumber += numbers 
    numbers += 1 
print(endNumber) 