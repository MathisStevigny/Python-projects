#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
max = 101
xSquared = 0
totalSquared = 0

for x in range(max):
    xSquared += x**2
for i in range(max):
    totalSquared += i
total = totalSquared**2 - xSquared

#end result
print(total)