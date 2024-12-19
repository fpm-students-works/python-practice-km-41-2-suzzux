def fact(n):
    new_n = int(n)
    if n < 0 or new_n != n:
        return 'Число повинно бути натуральним'
    else:
        result = 1
        for i in range(1, new_n + 1):
            result *= i
        return result