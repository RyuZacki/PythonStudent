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


