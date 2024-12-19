def root2(x):
    if x >= 0:
        result = x ** 0.5
        return result
    else:
        return "Число повинно бути невід'ємним"
        
def root3(x):
    result = round(abs(x) ** (1/3), 12)
    if x < 0:
        result *= -1
    return result