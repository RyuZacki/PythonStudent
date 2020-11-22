import math

#-----------------------------------------------------------------------------------------------------------------------

#Задача №1
def arithmetic(a, b, c):
    if c == '+':
        x = a + b
        print(x)
        return x
    elif c == '-':
        x = a - b
        print(x)
        return x
    elif c == '*':
        x = a * b
        print(x)
        return x
    elif c == '/':
        x = a / b
        print(x)
        return x
    else:
        print('Вы ввели не то значение!')


a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = input('ведите знак операции c: ')

arithmetic(a, b, c)

#-----------------------------------------------------------------------------------------------------------------------

#Задача №2
def is_year_leap(x):
    if x % 4 == 0:
        print('{0} - год високосный!'.format(x))
    elif x % 100 == 0:
        print('{0} - год високосный!'.format(x))
    elif x % 400 == 0:
        print('{0} - год високосный!'.format(x))
    else:
        print('Год не високосный!')

a = int(input('ведите год: '))
is_year_leap(a)

#-----------------------------------------------------------------------------------------------------------------------

#Задача №3
def square(x):
    Per = 4 * x
    print('Периметр квадрата равен {0}'.format(Per))

    Plo = x**2
    print('Площадь квадрата равна {0}'.format(Plo))

    Dig = 2 * x**2
    Dig1 = math.sqrt(Dig)
    print('Диагональ квадрата равна {0}'.format(Dig1))

a = int(input('Введите число a: '))
square(a)

#-----------------------------------------------------------------------------------------------------------------------

#Задача №4
Winter = [1, 2, 12]
Spring = [3, 4, 5]
Summer = [6, 7, 8]
Fall = [9, 10, 11]

def season(x):
    for i in Winter:
        if x == i:
            print('Сейчас зима') # if month in (12, 1, 2):
    for j in Spring:
        if x == j:
            print('Сейчас весна') # if month in (3, 4, 5):
    for k in Summer:
        if x == k:
            print('Сейчас лето') # if month in (6, 7, 8):
    for n in Fall:
        if x == n:
            print('Сейчас осень') # if month in (9, 10, 11):

a = int(input('Введите число месяца: '))
season(a)

#-----------------------------------------------------------------------------------------------------------------------

#Задача №5
def bank(a, years):
    i = 0
    while i <= years - 1:
        i += 1
        x = (a * 10)/100
        a = x + a

    print('Ваша сумма {0}, за {1} лет(год/года)'.format(a, years))

a = int(input('Введите сумму которую хотите занести: '))
b = int(input('Введите срок вклада: '))

bank(a, b)

#-----------------------------------------------------------------------------------------------------------------------

#Задача №6
def is_prime(number):

    if number == 1:
        print('False')
        return False

    for possible_divisor in range(2, number):
        if number % possible_divisor == 0:
            print('False')
            return False

    print('True')
    return True

a = int(input('Введите число: '))
is_prime(a)

#-----------------------------------------------------------------------------------------------------------------------

#Задача №7
def is_year_leap(year):

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False


def date(day, month, year):
    day_in_month = {1: 31,
                    2: 29 if is_year_leap(year) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True
    return False

a = int(input('Введите день!'))
b = int(input('Введите месяц!'))
c = int(input('Введите год!'))

date(a, d, c)

#-----------------------------------------------------------------------------------------------------------------------

#Задача №8
# A + B = C

def sum(a, b):
    c = a + b
    print("Сумма чисел A и B равна {0}".format(c))

a3 = int(input("Число A: "))
b3 = ont(input("Число B: "))

sum(a3, b3)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 9
# Сумма

def sum1(x):
    y = 0
    for i in range(x + 1):
        y = y + i

    print("Полученное число: " + str(y))

A = int(input("Введите число, сумму которого хотите получить: "))
sum1(A)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 10
#Пятью пять - двадцать пять

def sum2(x):
    print("Полученое числое: " + str(x**2))

A1 = int(input("Введите число, которое хотите возвести в квадрат: "))
sum2(A1)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 11
# Фактариал

def sum3(x):
    y = 1
    for i in range(x):
        i += 1
        y = y * i

    print("Полученное число: " + str(y))

A = int(input("Введите число, сумму которого хотите получить: "))
sum1(A)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 12
# Больше-меньше

def sum4(x, y):
    if x > y:
        print("Число {0}, больше чем {1}".format(x, y))
    elif x < y:
        print("Число {0}, меньше чем {1}".format(x, y))
    elif x == y:
        print("Число {0}, равно числу {1}".format(x, y))
    else:
        print("Мы не знаем что с этим делать")

A4 = int(input("Введите первое число: "))
B4 = int(input("Введите второе число: "))

sum4(A4, B4)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 13
# Бинарные числа

def sum5(x, y):
    value = True
    while value:
        if x % 2 == 0:
            if x == 2:
                print("Число {0}, является бинарным".format(y))
                value = False
            else:
                x = x / 2
        else:
            print("Число {0}, не бинарное".format(y))
            value = False

A5 = int(input("Введите число, для проверки его на бинарность: "))
B5 = A5
sum5(A5, B5)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 14
# От перестановки что-то меняется ...

def sum6(x, y, z):
    if x + y == z:
        print("True")
    elif x + z == y:
        print("True")
    elif y + z == x:
        print("True")
    else:
        print("False")

A6 = int(input("Введите число A: "))
B6 = int(input("Введите число B: "))
C6 = int(input("Введите число C: "))

sum6(A6, B6, C6)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 15
# Разворот

def sum7(x):
    print(x[::-1])

A8 = input("Введите значение которое хотите перевернуть: ")
sum7(A8)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 16
# Четырехзначный палиндром

def sum8(x):
    array1 = []
    if len(x) == 4:
        for i in x:
            array1.append(i)
        if array1[0] == array1[3]:
            if array1[1] == array1[2]:
                print("Число " + str(x) + ", является четырёхзначным палиндромом")
        else:
            print("Число " + str(x) + ", не является четырёхзначным палиндромом")
    else:
        print("Данное число, не является четырёхзначным")

A9 = input("Введите значение: ")
sum8(A9)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 17
# Единицы

def sum9(x):
    x1 = x
    binary_code = []
    units = []
    while True:
        if x % 2 == 1:
            x = (x - 1) / 2
            binary_code.append(1)
        elif x % 2 == 0:
            x = x / 2
            binary_code.append(0)

        if x == 1:
            binary_code.append(1)
            break
        elif x == 0:
            binary_code.append(0)
            break

    binary_code.reverse()

    for i in binary_code:
        if i == 1:
            units.append(1)
        else:
            continue

    P = len(units)
    print("В числе {0}, {1} двоичных единиц".format(x1, P))

A8 = int(input('Введите значение: '))
sum9(A8)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 18
# Числа Фибоначчи

def sum10(x):
    f1 = f2 = 1

    print(f1, end=' ')
    print(f2, end=' ')

    for i in range(2, x):
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')

A9 = int(input("Определите диапозон определения чисел фибоначчи: "))
sum10(A9)

#-----------------------------------------------------------------------------------------------------------------------

# Задача 19
#


