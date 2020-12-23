import math
import sys

print('Выполнил: Акимкин Максим ИУ5ц-72Б')
print()
if len(sys.argv) != 1: 
    for param in sys.argv:
        print(param, end=' ')
print()

A = 0
B = 0
C = 0
D = 0
X1 = 0
X2 = 0

cont = True

def getnumber(str, num):
    result = 0
    try:
        result = int(sys.argv[num])
    except BaseException:
        while True:
            try:
                result = int(input('Введите число {}: '.format(str)))
            except BaseException:
                print('Давай по новому! ')
                continue
            return result
            

while cont:
    A = getnumber('A', 1)
    B = getnumber('B', 2)
    C = getnumber('C', 3)

    print('Ваши числа:',A,B,C)

    # Основная логика квадратного уравнения
    if A!=0 and B!=0 and C!=0:
        D = B*B - 4*A*C
        print('Дискреминант =', D)
        if D  <0:
            print('Корней нет!')
        if D == 0:
            X1 = -B/(2*A)
            print('Корень уравнения:', X1)
        if D > 0:
            X1 = (-B + math.sqrt(D))/(2*A)
            X2 = (-B - math.sqrt(D))/(2*A)
            print('Корени уравнения:', X1, X2)
    elif A!=0 and B==0 and C==0:
        print('Корень уравнения:', 0)
    elif A!=0 and B==0 and C!=0:
        xx = -C/A
        if xx > 0:
            X1 = math.sqrt(xx)
            X2 = -math.sqrt(xx)
            print('Корени уравнения:', X1, X2)
        else:
            print('Корней нет!')
    elif A!=0 and B!=0 and C==0:
        X1 = 0
        X2 = -C/B
        print('Корени уравнения:', X1, X2)

    print('Продолжить?(1/0):')
    while True:
        try:
            cont = int(input('Введите число 1 для повтора или 0 для выхода: '))
        except BaseException:
            print('Давай по новому!')
            continue
        if cont != 1 and cont != 0:
            print('Давай по новому!')
            continue
        break
    print()
    print()
        
