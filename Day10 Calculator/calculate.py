def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

operator_function = {
    '+': addition,
    '*': multiplication,
    '-': subtraction,
    '/': division
}


def calculate(a, operator, b):
    return operator_function[operator](a, b)





