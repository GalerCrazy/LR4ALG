from calculus import *

a = "Tables/a.xlsx"
b = "Tables/b.xlsx"
while True:
    n = input("1. Умножение - 0\n2. Сложение - 1\n3. Вычитание - 2\n4. Симметричное вычитание - 3\n5. Выход - любое значение\n")
    if n not in {'0','1','2','3'}:
        break
    res = calculus(a,b,int(n))
    print(res)