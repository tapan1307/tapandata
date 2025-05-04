# Task 1:

def factorial(n):
    if(n<=1):
        return 1
    else:
        return n*factorial(n-1)

result=factorial(5)
print('Factorial of ',5,' is',result )

# Task 2;

import math
x=int(input('Enter a number: '))
print("Square root is", math.sqrt(x))
print("Logarithm is", math.log(x))
print("Sine is ", math.sin(x))
