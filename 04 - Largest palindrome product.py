'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''
number1 = 100
number2 = 100
array = []

while number1 * number2 < 998001:
    if str(number1 * number2) == str(number1 * number2)[::-1]:
        largestPalindrome = number1 * number2
        array.append(largestPalindrome)
        #print(largestPalindrome)
    if number1 < 999:
            number1 += 1
    else:
        number1 = 100
        number2 += 1

#end result
print(max(array))