import math

def log(a, b):
    if a <= 0 or a == 1:
        return 'Невалідна основа'
    elif b <= 0:
        return 'Невалідний аргумент'
    else:
        return math.log(b, a)
    
def ln(b):
    if b <= 0:
        return 'Невалідний аргумент'
    else:
        return math.log(b)
    
def lg(b):
    if b <= 0:
        return 'Невалідний аргумент'
    else:
        return math.log10(b)