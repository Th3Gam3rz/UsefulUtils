def specialRound(number, rounding):
    """A method used to round a number in the way that UsefulUtils rounds."""
    temp = 0
    if rounding == 0:
        temp = number
    else:
        temp =  round(number, rounding)
    if temp % 1 == 0:
        return int(temp)
    else:
        return float(temp)

def root(number, power, rounding=0):
    return specialRound(number**(1/power), rounding)

def power(number, power, rounding=0):
    if power == 0: return int(1)
    return specialRound(number**power, rounding)

def sqr(number, rounding=0):
    return specialRound(number**2, rounding)

def sqrRoot(number, rounding=0):
    return specialRound(number**0.5, rounding)

def cube(number, rounding=0):
    return specialRound(number**3, rounding)

def cubeRoot(number, rounding=0):
    return specialRound(number**(1/3), rounding)

def sumOf(numbers, rounding = 0):
    temp = 0
    for number in numbers: temp += float(number)
    return specialRound(temp, rounding)

def add(number1, number2, rounding=0):
    return specialRound(number1+number2, rounding)

def subtract(number1, number2, rounding=0):
    return specialRound(number1-number2, rounding)

def subtractLess(number1, number2, rounding=0):
    if number2 < number1:
        return specialRound(number1-number2, rounding)
    else:
        return specialRound(number2-number1, rounding)

def subtractMore(number1, number2, rounding=0):
    if number2 > number1:
        return specialRound(number1-number2, rounding)
    else:
        return specialRound(number2-number1, rounding)

def multiply(number1, number2, rounding=0):
    return specialRound(number1*number2, rounding)

def divide(number1, number2, rounding=0):
    return specialRound(number1/number2, rounding)

def divideLess(number1, number2, rounding=0):
    if number2 < number1:
        return specialRound(number1/number2, rounding)
    else:
        return specialRound(number2/number1, rounding)

def divideMore(number1, number2, rounding=0):
    if number2 > number1:
        return specialRound(number1/number2, rounding)
    else:
        return specialRound(number2/number1, rounding)
