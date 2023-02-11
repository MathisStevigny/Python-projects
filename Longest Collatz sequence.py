#Which starting number, under one million, produces the longest chain?
startingNumber = 1
currentNumber = 0
longestLength = 0
lastHighTerm = 0
length = 0
while startingNumber < 1000000:
    currentNumber = startingNumber
    while currentNumber != 1:
        if currentNumber % 2 == 0:
            currentNumber /= 2
            length += 1
        else:
            currentNumber *=3
            currentNumber +=1
            length += 1
    if length > longestLength:
        longestLength = length
        lastHighTerm = startingNumber
        print(lastHighTerm)
    startingNumber += 1
    length = 0
print(longestLength+1)
print(lastHighTerm)