from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    func = int(input('''Оберіть бажану функцію:
1 — факторіал;
2 — піднесення до 2 степеня;
3 — піднесення до 3 степеня;
4 — обчислення квадратного кореня;
5 — обчислення кореня 3 степеня;
6 — обчислення логарифма з довільною основою;
7 — обчислення натурального логарифма;
8 — обчислення десяткового логарифма

'''))
    if func == 1:
        n = float(input('Введіть значення аргументу функції: '))
        print(fact(n))
    elif func == 2:
        x = float(input('Введіть значення аргументу функції: '))
        print(exp2(x))
    elif func == 3:
        x = float(input('Введіть значення аргументу функції: '))
        print(exp3(x))
    elif func == 4:
        x = float(input('Введіть значення аргументу функції: '))
        print(root2(x))
    elif func == 5:
        x = float(input('Введіть значення аргументу функції: '))
        print(root3(x))
    elif func == 6:
        a = float(input('Введіть значення основи логарифма: '))
        b = float(input('Введіть значення аргументу функції: '))
        print(log(a, b))
    elif func == 7:
        b = float(input('Введіть значення аргументу функції: '))
        print(ln(b))
    elif func == 8:
        b = float(input('Введіть значення аргументу функції: '))
        print(lg(b))
        
main()