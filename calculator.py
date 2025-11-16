# https://github.com/sair9991/lab11---SR---DD.git

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Can't take square root of negative num.")
        return math.sqrt(a)
    except TypeError:
        raise TypeError
    
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError
    
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError
    return math.log(b, a)
    
def exp(a, b):
    return a ** b
