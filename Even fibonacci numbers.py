first = 1
second = 2
third = 0
end = 2
while third < 4000000:
    if third/2 == int(third/2):
        end += third
    third = second + first
    first = second
    second = third
print (first)
print(second)
print(third)
print(end)