import math

print(10 * 3)   # multiplication
print(10 - 3)   # subtraction
print(10 + 3)   # addition
print(10 / 3)   # division
print(10 // 3)  # returns an integer
print(10 % 3)   # returns a remainder
print(10 ** 3)  # exponent, so 10 to the power of 3

#   working with assignment operators 
x = 10
x = x + 3
print(x)

#   augmented assignment operator
x += 3
print(x)

x -= 3
print(x)

#   operator precedence 
x = 10 + 3 * 2
#   in the arithmetic above, the * takes precedence
#   it works like the BODMAS way of giving precendence to and operation
#   the solution to this should be 10 + 6 which is 16 
print(x)

#   order of precedence
#   parenthesis
#   exponentiation like 2 ** 3
#   multiplication or division
#   addition or subtraction
x = 10 + 3 * 2 ** 2
print(x)

#   Math functions
x = 2.9
print(round(x))     # rounds up
print(abs(-x))      # disregards the negative sign

#   making using of reusable functions from the math module (import math in first line)
print(math.ceil(2.9))
print(math.floor(2.9))

