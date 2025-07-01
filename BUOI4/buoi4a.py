import math

from sympy.utilities.lambdify import MATH

a = 5
b = 6
c = 7
def square(a):
    return a*a
print("a^2 = ",square(a))

def rectangle(a, b):
    return a*b
print("S rectangle = ",rectangle(a,b))

def triangle(a, b, c):
    s = (a + b + c)/2
    return math.sqrt(s *(s - a)*(s - b)*(s - c))
print("S triangle =", triangle(a, b, c))

def factorial(a):
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result
print(factorial(a))

def multiplication_table(a):
    for i in range(1, 11):
        print(a,"*" ,i , "=", a*i)

multiplication_table(a)





